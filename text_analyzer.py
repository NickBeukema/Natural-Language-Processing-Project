import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from bs4 import BeautifulSoup
import re

class TextAnalyzer:
  SENTENCE_SPLIT_REGEX = r'[.!?]+'

  WORD_OVER_SENTENCE_CONSTANT = 1.015
  SYLLABLE_OVER_WORD_CONSTANT = 84.6
  TOTAL_CONSTANT = 206.835

  STOP_WORDS = set(stopwords.words('english'))
  BANNED_WORDS = [
    'meth',
    'methedrine',
    'methamphetamine_hydrochloride',
    'deoxyephedrine'
  ]

  def __init__(self, text):
    self.initialText = text
    self.tokens = self.initialText.split()
    self.syllableDictionary = {}

  def fullPass(self):
    self.calculate()
    self.display()

  def calculate(self):
    self.sentenceCount = len(re.split(self.SENTENCE_SPLIT_REGEX, self.initialText))

    self.tokens = self.initialText.split()
    self.syllableCount = self.__countAllSyllables(self.tokens)
    self.wordCount = len(self.tokens)

    # Sentence Length Ratio
    part1 = self.WORD_OVER_SENTENCE_CONSTANT * (self.wordCount / self.sentenceCount)

    # Word Length Ratio
    part2 = self.SYLLABLE_OVER_WORD_CONSTANT * (self.syllableCount / self.wordCount)

    self.score = self.TOTAL_CONSTANT - part1 - part2

  def display(self):
    print("Sentence Count:\t" + str(self.sentenceCount))
    print("Word Count:\t" + str(self.wordCount))
    print("Syllable Count:\t" + str(self.syllableCount))

    print("Score:\t\t" + str(self.score))
    print("Classification:\t" + self.__classifyText())



  def upgrade_word(self, taggedWord, upgrade=True):

    # Pull word from passed in word with tag
    word = taggedWord[0]

    # Setup initial variables for finding best candidate,
    # defaulting to the original word
    syllableGoal = self.__countSyllablesInWord(word)
    bestCandidate = word
    
    # Make sure there are actually synonym sets
    if len(wn.synsets(word)) > 0:
      
      #
      # Goal: iterate across synonyms and return the word with the most synonyms
      #


      # Extract the basic word type (eg. VBN => .v.)
      # the latter appears inside a synsets name (playing.v.1)
      # and we need to make sure we're grabbing the correct types
      wordType = taggedWord[1][0].lower()
      wrappedWordType = '.' + wordType + '.'

      # All synsets with the same type
      syns = [syn for syn in wn.synsets(word) if wrappedWordType in syn.name()]

      # Extrapolate all lemma names for each synset into one list
      allOptions = [item for sublist in [sim.lemma_names() for sim in syns] for item in sublist]

      # Remove all occurances of the original word from the list
      filteredOptions = [option for option in allOptions if option != word]

      # Only use unique values
      uniqOptions = list(set(filteredOptions))

      # Some words in the dictionary are rediculously long, prune these out
      prunedForLongWords = [pruned for pruned in uniqOptions if len(pruned) < 15]

      # Some words are just not okay
      prunedForBannedWords = [w for w in prunedForLongWords if w.lower() not in self.BANNED_WORDS]

      for option in prunedForBannedWords:

        syllables = self.__countSyllablesInWord(option)

        # Check if the current word beats the best candidate so far, whether looking
        # for an upgrade or a downgrade
        betterCandidate = (syllables > syllableGoal) if upgrade else (syllables < syllableGoal)

        if betterCandidate:
          bestCandidate = option
          syllableGoal = syllables

    # After all iterations, we return the best candidate, or the
    # original word if none are found
    return bestCandidate.replace('_', ' ')



  # Default augmentation to upgrading, if downgrading is desired,
  # pass in False instead
  def augment(self, upgrade=True):

    # 1. Determine what words NOT to change (aka proper nouns, numbers in them, certian phrases aka gold medal?)
    # 2. How many of the left over words to "upgrade" -- to what degree? (college, or just 7th grade?)
    # 3. Find similar words for each of the words to upgrade, making sure the new word has more syllables
    # 4. Profit

    nouns = 0
    verbs = 0
    articles = 0

    # Tag the tokenzid version of the text w/ the POS of each word
    tagged = nltk.pos_tag(self.tokens)

    for word in tagged:

      wordType = word[1]
      wordText = word[0]


      # Do not replace proper nouns or stop words
      if 'NNP' in wordType or wordText in self.STOP_WORDS:
        continue

      # Nouns
      if 'NN' in wordType:
        nouns += 1
        # Replace all instances of the word in the text

        # TODO: This causes bugs because it replaces all occurances, and
        # can potentially cause repeating words with the right combination
        #
        # eg. ice hockey, ice upgrades to water, and hocky upgrades to ice hockey
        # later down the article if ice gets upgraded again, the ice hockey gets
        # changed to water hockey, resulting in water water hockey
        #
        self.initialText = self.initialText.replace(wordText, self.upgrade_word(word, upgrade))

      # Verbs
      elif 'VB' in wordType:
        verbs += 1
        # Replace all instances of the word in the text
        self.initialText = self.initialText.replace(wordText, self.upgrade_word(word, upgrade))






  def __countAllSyllables(self, tokens):
    return sum([ val for val in [self.__countSyllablesInWord(word) for word in tokens] if val is not None])

  # https://codegolf.stackexchange.com/a/47326
  def __countSyllablesInWord(self, word):
    return len(''.join(c if c in"aeiouy"else' 'for c in word.rstrip('e')).split())

  def __classifyText(self):
    if self.score is None:
      return None
    elif self.score >= 90:
      return "5th Grade"
    elif self.score >= 80 and self.score < 90:
      return "6th Grade"
    elif self.score >=70 and self.score < 80:
      return "7th Grade"
    elif self.score >=60 and self.score < 70:
      return "8th & 9th Grade"
    elif self.score >=50 and self.score < 60:
      return "10th to 12th Grade"
    elif self.score >=30 and self.score < 50:
      return "College"
    else:
      return "College Graduate"

# taggedWord = ('playing', 'VBG')
# ta = TextAnalyzer('playing')
# ta.upgrade()

# ta2 = TextAnalyzer('Just call it a sister thing. Whenever another hockey team has sisters on the rosters, Jocelyne Lamoureux-Davidson and Monique Lamoureux-Morando take notice')

# ta2.calculate()
# ta2.display()

# ta2.upgrade()
# ta2.calculate()
# ta2.display()

# import pdb; pdb.set_trace()
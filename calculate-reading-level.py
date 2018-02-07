from urllib.request import urlopen
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import re

# https://codegolf.stackexchange.com/a/47326
def countSyllables(word):
  return len(''.join(c if c in"aeiouy"else' 'for c in word.rstrip('e')).split())

def calcScore(wordList, sentenceCount):
  totalWords = len(wordList)
  totalSyllables = sum([ val for val in [countSyllables(word) for word in wordList] if val is not None])

  part1 = 1.015 * (totalWords / sentenceCount)
  part2 = 84.6 * (totalSyllables / totalWords)

  print("Word Count: " + str(totalWords))
  print("Syllable Count: " + str(totalSyllables))
  print("Sentence Count: " + str(sentenceCount))

  return 206.835 - part1 - part2




# Higher Reading Level
# response = urlopen('https://news.ycombinator.com/item?id=16325195')
# response = urlopen('https://en.wikipedia.org/wiki/Guadalcanal_Campaign')

# Middle Reading Level
# response = urlopen('https://www.npr.org/sections/13.7/2018/02/01/581864513/would-college-students-retain-more-if-professors-dialed-back-the-pace')

# Lower Reading Level
# response = urlopen('http://www.magickeys.com/books/gingerbread/index.html')
response = urlopen('https://www.dogonews.com/2018/2/5/meet-pigcasso-the-worlds-first-pig-artist')




html = response.read().decode('utf-8')
print(len(html))

clean = BeautifulSoup(html, 'html.parser').find('body').get_text()
tokens = [tok for tok in clean.split()]

print(clean)

stopWords = list(stopwords.words('english'))
regexToAvoid = r'[\[\]\(\)\{\}\\\/:]|www|http|\d'



# Strip all single characters and any stopwords
clean_tokens = [tok for tok in tokens if len(tok.lower()) > 1 and (tok.lower() not in stopWords) and not (re.search(regexToAvoid, tok)) and len(tok.lower()) < 20]
print("Total no of tokens: " + str(len(clean_tokens)))
# print(clean_tokens[0:100])

print(clean_tokens)

freq = nltk.FreqDist(clean_tokens)

sentences = len(re.split(r'[.!?]+', clean))
# print(sentences)

score = calcScore(clean_tokens, sentences)
print(score)

# for k,v in freq.items():
#   print(str(k) + ':' + str(v))

freq.plot(50, cumulative=False)



# print(syll("beukema"))

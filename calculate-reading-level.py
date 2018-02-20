from text_analyzer import TextAnalyzer
from nltk.corpus import wordnet as wn



def countSyllablesInWord(word):
  return len(''.join(c if c in"aeiouy"else' 'for c in word.rstrip('e')).split())

def upgradeWord(word):
  all = [item for sublist in [sim.lemma_names() for sim in wn.synsets(word)] for item in sublist]
  winner = None
  val = 0

  for w in all:
    c = countSyllablesInWord(w)
    if c > val:
      winner = w
      val = c

  return winner

  

# with open('text/meditations.txt', 'r') as textFile:
#   data=textFile.read().replace('\n', '')

# with open('text/kid-article-1.txt', 'r') as textFile:
#   data=textFile.read().replace('\n', '')

with open('text/quran.txt', 'r') as textFile:
  data=textFile.read().replace('\n', '')



splitWords = data.split()
wordLength = len(splitWords)

datas = {}

rangeCount = 10
rangeAmount = wordLength // rangeCount


for x in range(0, rangeCount):
  start = x * rangeAmount
  end = start + rangeAmount

  txt = ' '.join(splitWords[start:end])
  print("Words: " + str(start) + " - " + str(end))

  ta = TextAnalyzer(txt)
  ta.calculate()
  datas[x] = ta

  ta.fullPass()

  print("\n\n")




# splitData = " ".join(data.split()[1000:2000])

taMain = TextAnalyzer(data)
taMain.calculate()
taMain.display()

import pdb; pdb.set_trace()

taMain.augment(False)
taMain.calculate()
taMain.display()

import pdb; pdb.set_trace()
from urllib.request import urlopen
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

response = urlopen('https://www.npr.org/sections/13.7/2018/02/01/581864513/would-college-students-retain-more-if-professors-dialed-back-the-pace')
html = response.read().decode('utf-8')
print(len(html))

clean = BeautifulSoup(html, 'html.parser').get_text()
tokens = [tok for tok in clean.split()]

stopWords = set(stopwords.words('english'))

# Strip all single characters and any stopwords
clean_tokens = [tok for tok in tokens if len(tok.lower()) > 1 and (tok.lower() not in stopWords)]
print("Total no of tokens: " + str(len(clean_tokens)))
print(clean_tokens[0:100])

freq = nltk.FreqDist(clean_tokens)


for k,v in freq.items():
  print(str(k) + ':' + str(v))

freq.plot(50, cumulative=False)

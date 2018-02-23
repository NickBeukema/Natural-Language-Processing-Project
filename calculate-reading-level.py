
from text_analyzer import TextAnalyzer
from text_analyzer import TextManager
from text_analyzer import TextDataGrapher

# 
# Beowulf Comparison
# 
def beowulfCompare():
  tm1 = TextManager('text/beowulf1.txt', title = "Lesslie Hall")
  tm2 = TextManager('text/beowulf2.txt', title = "Gummere")

  tg = TextDataGrapher(textManagers = [tm1, tm2], title = "Comparison between Beowulf Translations")


#
# Bill Gates Augmentation
#
def billAugment():
  tm = TextManager('text/bill-gates.txt')
  tm.entireData.display()
  print(tm.entireData.initialText)

  tm.entireData.augment()
  tm.entireData.calculate()
  tm.entireData.display()
  print(tm.entireData.initialText)


def compareSixteenHundred():
  tm1 = TextManager('text/1600s/don-quixote.txt', title = "Don Quixote")
  tm2 = TextManager('text/1600s/the-pattern-of-painful-adventures.txt', title = "The Patterns of Painful Adventures")
  tm3 = TextManager('text/1600s/tom-a-lincoln.txt', title = "Tom a Lincoln")

  tg = TextDataGrapher(textManagers = [tm1, tm2, tm3], title = "Comparison between Texts of the 1600s")


def compareSeventeenHundred():
  tm1 = TextManager('text/1700s/gullivers-travels.txt', title = "Gulliver's Travels")
  tm2 = TextManager('text/1700s/captain-singleton.txt', title = "Captain Singleton")
  tm3 = TextManager('text/1700s/pamela-or-virtue-rewarded.txt', title = "Pamela or Virtue Rewarded")

  tg = TextDataGrapher(textManagers = [tm1, tm2, tm3], title = "Comparison between Texts of the 1700s")

def compareEighteenHundred():
  tm1 = TextManager('text/1800s/crime-and-punishment.txt', title = "Crime and Punishment")
  tm2 = TextManager('text/1800s/frankenstein.txt', title = "Frankenstein")
  tm3 = TextManager('text/1800s/pride-and-prejudice.txt', title = "Pride and Prejudice")

  tg = TextDataGrapher(textManagers = [tm1, tm2, tm3], title = "Comparison between Texts of the 1800s")

def compareNineteenHundred():
  tm1 = TextManager('text/1900s/the-jungle.txt', title = "The Jungle")
  tm2 = TextManager('text/1900s/the-major.txt', title = "The Major")
  tm3 = TextManager('text/1900s/to-kill-a-mockingbird.txt', title = "To Kill a Mockingbird")

  tg = TextDataGrapher(textManagers = [tm1, tm2, tm3], title = "Comparison between Texts of the 1900s")

def compareTwoThousand():
  tm1 = TextManager('text/2000s/harry-potter.txt', title = "Harry Potter")
  tm2 = TextManager('text/2000s/hunger-games.txt', title = "Hunger Games")
  tm3 = TextManager('text/2000s/the-kite-runner.txt', title = "The Kite Runner")

  tg = TextDataGrapher(textManagers = [tm1, tm2, tm3], title = "Comparison between Texts of the 2000s")

def augmentOurPaper():
  tm = TextManager('text/writeup.txt')
  tm.entireData.display()
  print(tm.entireData.initialText)

  tm.entireData.augment()
  tm.entireData.calculate()
  tm.entireData.display()
  print(tm.entireData.initialText)

augmentOurPaper()
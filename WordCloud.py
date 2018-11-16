import collections
import inline as inline
import matplotlib.pyplot as plt
import numpy as np
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
text = open('98-0.txt')

class word_cloud:
  def __init__(self):
      self.document = open('98-0.txt')
      self.wordcount = {}
      self.sorted_wordcount = {}
      self.stopwords = set(line.strip() for line in open('stopwords'))

  def process_words(self):
      for word in self.document.read().lower().split():
          word = word.replace(".", "")
          word = word.replace(",", "")
          word = word.replace('"', "")
          word = word.replace("'", "")
          word = word.replace('\\', "")
          word = word.replace("(", "")
          word = word.replace(")", "")
          word = word.replace(";", "")
          word = word.replace("-", "")
          word = word.replace("!", "")
          word = word.replace("?", "")
          word = word.replace(":", "")
          if word not in self.stopwords:
              if word not in self.wordcount:
                  self.wordcount[word] = 1
              else:
                  self.wordcount[word] += 1
      self.sorted_wordcount = collections.Counter(self.wordcount)

  def most_common(self):
      for word, count in self.sorted_wordcount.most_common(10):
          print (word, ": ", count)


class Tester:
  def __init__(self):
      self.case = word_cloud()
      self.case.process_words()

  def return_words(self):
      return self.case.most_common()


tester = Tester()
print tester.return_words()


WordsToShow = text.read()
cloud = WordCloud().generate(WordsToShow)

plt.imshow(cloud, interpolation='bilinear')
plt.axis("off")
plt.show()

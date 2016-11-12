import nltk.data
import re
mystr = 'Why doesnt this work'
words = re.sub("[^\w]", " ",  mystr).split()
classifier = nltk.data.load('classifiers/movie_reviews_NaiveBayes.pickle')
print words
feats = dict([(word, True) for word in words])
print classifier.classify(feats)
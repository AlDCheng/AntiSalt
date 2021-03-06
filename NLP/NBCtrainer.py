import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk import *

def word_feats(words):
    return dict([(word,True) for word in words])

def return_classifier(stat=False):
    negids = movie_reviews.fileids('neg')
    posids = movie_reviews.fileids('pos')
    
    negfeats = [(word_feats(bigrams(movie_reviews.words(fileids=[f]))), 'neg') for f in negids]
    posfeats = [(word_feats(bigrams(movie_reviews.words(fileids=[f]))), 'pos') for f in posids]

    negcutoff = len(negfeats)*3/4
    poscutoff = len(posfeats)*3/4

    trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
    testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]

    classifier = NaiveBayesClassifier.train(trainfeats)
    if stat: 
        print 'train on %d instances, test on %d instances' % (len(trainfeats),len(testfeats))
        print 'accuracy:', nltk.classify.util.accuracy(classifier,testfeats)
        classifier.show_most_informative_features()     
    return classifier

def classify_sentence(text):
    words = re.sub("[^\w]", " ",  text).split()
    set = return_classifier().classify(words)
    if set == 'neg':
        k = random.randint(50,100)
    elif set == 'pos':
        k = random.randint(1,50)
    return k
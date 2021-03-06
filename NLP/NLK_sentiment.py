import nltk.data
import re
import random
import os 

def classify_sentence(mystr):
    #mystr = raw_input('Why doesnt this work?')
    words = re.sub("[^\w]", " ",  mystr).split()
    classifier = nltk.data.load("movie_reviews_NaiveBayes.pickle")
    feats = dict([(word, True) for word in words])
    set = classifier.classify(feats)
    if set == 'neg':
        k = random.randint(1,10)
    elif set == 'pos':
        k = random.randint(-5,0)
    return k

"""
from nltk import *
from nltk.corpus import sentiwordnet as swn

def pos_assign(tag):
    if tag in ['NN','NNP','NNS','PRP','PRP$','WP']:
        return 'n'
    elif tag in ['VB','VBD','VBG','VBN','VBP','VBZ']:
        return 'v'
    elif tag in ['JJ','JJR','JJS']:
        return 'a'
    elif tag in ['RB','RBR','RBS','WRB']:
        return 'r'

def classify_sentence(words):
    ttext = pos_tag(word_tokenize(words))
    negatives = ['not', 'no']
    pos,neg = (0,0)
    neg_counter = 0
    for i in xrange(len(ttext)):
        word,tag = ttext[i][0],ttext[i][1]
        try:
            if word in negatives:
                neg_counter += 1
                continue
            score = swn.senti_synset('{}.{}.01'.format(word,pos_assign(tag)))
            if ttext[i-1][0] in negatives:
                pos += score.neg_score()

                neg += score.pos_score()
                continue
            pos += score.pos_score()
            neg += score.neg_score()
        except: pass
    effective_total = len(ttext) - neg_counter
    pos = pos/effective_total
    neg = neg/effective_total
    return (pos - neg)
def get_nltk_algonumber():
    word = raw_input('Chat log: ')
    current_algonumber = float(classify_sentence(word))
    if current_algonumber>=0:
        return (100*current_algonumber)
    else:
        return ((100*current_algonumber)+100)
"""
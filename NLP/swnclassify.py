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
    negatives = ['not','no']
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
    return pos - neg
from nltk import *
from nltk.corpus import sentiwordnet as swn

def classify_sentence(word_list):
    ttext = pos_tag(word_list)
    noun_tags = ['NN','NNP','NNS','PRP','PRP$','WP']
    verb_tags = ['VB','VBD','VBG','VBN','VBP','VBZ']
    adjective_tags = ['JJ','JJR','JJS']
    adverb_tags = ['RB','RBR','RBS','WRB']
    pos,neg = (0,0)
    for word,tag in ttext:
        try: 
            if tag in noun_tags:score = swn.senti_synset('{}.{}.01'.format(word,'n'))
            elif tag in verb_tags:score = swn.senti_synset('{}.{}.01'.format(word,'v'))
            elif tag in adjective_tags:score = swn.senti_synset('{}.{}.01'.format(word,'a'))
            elif tag in adverb_tags:score = swn.senti_synset('{}.{}.01'.format(word,'r'))
            pos += score.pos_score()
            neg += score.neg_score()
        except: pass
    pos = pos/len(ttext)
    neg = neg/len(ttext)
    return pos - neg


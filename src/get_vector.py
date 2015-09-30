__author__ = 'arkanath'

from nltk.corpus import wordnet as wn
import nltk
import umbc

categories = ["hate", "love"]
# categories = ["fight", "love", "respect", "action", "trust", "mistrust"]
causes = {}
causes['hate'] = ["hate"]
causes['love'] = ["love"]
# causes['fight'] = ['fight', 'tears', 'disappoint']
# causes['love'] = ['love', 'kiss']
# causes['respect'] = ['respect', 'chants', 'instruct', 'master', 'kneel', 'order']
# causes['action'] = ['action', 'victory', 'defend', 'horse', 'sword', 'gun', 'quickly', 'cheers']
# causes['trust'] = ['trust', 'friend', 'save']
# causes['mistrust'] = ['mistrust', 'deceive', 'concern', 'surprise']

# wn_synsets = {}
#
# def init_wn_synsets():
#     for c in categories:
#         for l in causes[c]:
#             wn_synsets[l] = wn.synsets(l)[0]
#             print l,wn.synsets(l)
#
# print (wn.synsets('scorn')[0]).lemma_names()

memo = {}

def get_vector(tokens):
    ret = [0.0,0.0]
    i=0
    for c in categories:
        for l in tokens:
            if (l,c) not in memo:
                memo[(l,c)] = umbc.get_umbc_similarity(l,c)
                if(memo[(l,c)]<0.0):
                    memo[(l,c)]=0.0
                # print l,c,memo[(l,c)]
            ret[i] += memo[(l,c)]
        i+=1
    # print ret
    return ret
    # return categories[max(enumerate(ret), key=lambda x:x[1])[0]]

# print 'scorn', get_vector(['scorn','love'])
# print 'kills', get_vector('kills')
# print 'crushes', get_vector('crushes')
# print 'summons', get_vector('summons')
# print 'eats', get_vector('eats')
# print 'annoys', get_vector('annoys')
# print 'chases', get_vector('chases')
# print 'sleeps', get_vector('sleeps')
# print 'ignores', get_vector('ignores')
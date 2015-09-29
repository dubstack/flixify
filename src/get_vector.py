__author__ = 'arkanath'

from nltk.corpus import wordnet as wn

categories = ["fight", "love", "respect", "action", "trust", "mistrust"]
causes = {}
causes['fight'] = ['fight', 'tears', 'disappoint']
causes['love'] = ['love', 'kiss']
causes['respect'] = ['respect', 'chants', 'instruct', 'master', 'kneel', 'order']
causes['action'] = ['action', 'victory', 'defend', 'horse', 'sword', 'gun', 'quickly', 'cheers']
causes['trust'] = ['trust', 'friend', 'save']
causes['mistrust'] = ['mistrust', 'deceive', 'concern', 'surprise']

wn_synsets = {}

def init_wn_synsets():
    for c in categories:
        for l in causes[c]:
            wn_synsets[l] = wn.synsets(l)[0]

def get_vector(word1):
    # print dog.lch_similarity(cat)
    # print dog.wup_similarity(cat)
    print word1
    
    dog = wn.synsets(word1)[0]
    ret = []
    for c in categories:
        max_score = 0
        for l in causes[c]:
            max_score = max(max_score, dog.path_similarity(wn_synsets[l]))
        ret.append(max_score)
    return ret
    # return categories[max(enumerate(ret), key=lambda x:x[1])[0]]

# print 'kiss', get_vector('kiss')
# print 'kills', get_vector('kills')
# print 'crushes', get_vector('crushes')
# print 'summons', get_vector('summons')
# print 'eats', get_vector('eats')
# print 'annoys', get_vector('annoys')
# print 'chases', get_vector('chases')
# print 'sleeps', get_vector('sleeps')
# print 'ignores', get_vector('ignores')
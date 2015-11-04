__author__ = 'arkanath'

from gensim.models import Word2Vec
from nltk.corpus import brown
import itertools
import logging
import numpy as np
import scipy

logger = logging.getLogger('root')
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)

def learn_word2vec(filename, sentences=brown.sents()):
    logger.debug("Training")
    model = Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)
    logger.debug("Trained, Saving")
    model.save("models/"+filename)
    logger.debug("Saved")

def load_word2vec(filename):
    model = Word2Vec.load("models/"+filename)
    return model

# learn_word2vec("learnt")
model = load_word2vec("learnt")
print "Loaded!"
print np.linalg.norm(np.array(model['dog']) - np.array(model['cat']))
print np.linalg.norm(np.array(model['dog']) - np.array(model['lion']))
print np.linalg.norm(np.array(model['dog']) - np.array(model['eat']))
print np.linalg.norm(np.array(model['dog']) - np.array(model['fur']))
print np.linalg.norm(np.array(model['dog']) - np.array(model['king']))
print model.most_similar(positive=['woman', 'king'], negative=['man'])
print model.most_similar(positive=['hate', 'love'], negative=['fly'])
# print 1-scipy.spatial.distance.cosine(model['hate']-model['love'],model['hate'])
# print 1-scipy.spatial.distance.cosine(model['hate']-model['love'],model['love'])

# print model.similarity('hate', 'envy')
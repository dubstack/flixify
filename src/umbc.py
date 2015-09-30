__author__ = 'arkanath'

import requests

def get_umbc_similarity(phrase1, phrase2, term=20):
    if(term==0):
        return 0.0
    url = "http://swoogle.umbc.edu/SimService/GetSimilarity"
    data = {"operation": "api", "phrase1": phrase1, "phrase2": phrase2, "type": "relation"}
    try:
        # print "trying request ",phrase1, phrase2
        s = requests.session()
        r = s.post(url, data)
    except requests.exceptions.ConnectionError:
        print "Connection Error, Trying Again"
        return get_umbc_similarity(phrase1, phrase2, term-1)
    return float(r.text)
    # print "found", r.text
from subtitleParser import get_subtitle_list_from_file
from category_scores import get_results
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import numpy as np
import json

flag_score = False
flag_anal = False
flag_train = True
window_size = 10
cat = ['posemo','anger','sexual','negemo','sad']

def calcScore():
    stop = stopwords.words('english') + ["scene change"] + ['.',',']
    subtitle_list = get_subtitle_list_from_file("../subtitles/el.srt")
    print "Subtitles Parsed..."
    iter = 0
    # print stop
    score = list()
    for el in subtitle_list:
        token = word_tokenize(el['text'])
        token = [x for x in token if x not in stop]
        words = dict()
        for to in token:
            to = to.lower()
            if words.has_key(to):
                words[to] = words[to] + 1
            else:
                words[to] = 1
        if len(words)==0:
            continue
        ret = get_results(words)
        ret['time']=el['time']
        score.append(ret)
    print "Scoring Done..."
    with open("data/emp.json","w+") as f:
        json.dump(score,f)
        print "Saved."

def analysis():
    with open('data/emp.json') as data_file:
        score = json.load(data_file)
    cum = list()

    print "calc"
    i = 0
    for i in range(1,len(score)):
        win = list()
        for c in cat:
            win.append(0)
        for j in range(i,min(i+100,len(score))):
            ci = 0
            for c in cat:
                win[ci] = win[ci] + score[j][c]
                ci = ci+1
        win = [x / window_size for x in win]
        cum.append(win)
    with open("data/cum.json","w+") as f:
        json.dump(cum,f)
        print "Saved."

def doKnn():
    with open('data/cum.json') as data_file:
        cum = json.load(data_file)
    ass = np.array(cum)
    from sklearn.cluster import KMeans
    km = KMeans(n_clusters=5)
    km.fit(X = ass)
    v = km.predict(ass)
    return v

def process():
    if flag_score:
        calcScore()
    if flag_anal:
        analysis()
    if flag_train:
        return doKnn()
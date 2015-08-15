__author__ = 'arkanath'

from nltk.tokenize import word_tokenize
import MySQLdb as mdb
import MySQLdb.cursors as curs
from subtitleParser import get_subtitle_list_from_file
import difflib
import copy

def levenshtein(a,b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n

    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)

    return current[n]

def tokenize(text):
    return [l for l in word_tokenize(text.lower()) if l != "-" and l!="."]
def find_nearest_time(subtitle_list, dialogue_text):
    nearest_time = ""
    max_sim = 0.0
    dialogue_list = tokenize(dialogue_text)
    for sub_entry in subtitle_list:
        time = sub_entry["time"]
        text = sub_entry["text"]
        sim = difflib.SequenceMatcher(None,tokenize(text),dialogue_list).ratio()
        # sim = levenshtein(tokenize(text.lower()),dialogue_list)
        # print sim, dialogue_list, tokenize(text.lower())
        # print sim, sub_entry
        if sim > max_sim:
            max_sim = sim
            nearest_time = time
    return nearest_time

def fill_dialogues_times():
    # TODO[@gaurav] fix the sql syntax according to the update table syntax
    subtitle_list = get_subtitle_list_from_file("/Users/arkanath/Dropbox/IIT-Kgp_Coursework/NLP/Project/flixify/subtitles/gladiator.srt")
    db = mdb.connect(host="10.5.18.68", user="12CS30010", passwd="dual12", db="12CS30010", cursorclass=curs.DictCursor, charset='utf8')
    cur = db.cursor()
    cur.execute('select * from scriptData where typ="dialogue"')
    data = cur.fetchall()
    for entry in data:
        # print entry['content']
        time = find_nearest_time(subtitle_list, entry['content'])
        if(time!=""):
            print entry['inde'], time
            cur.execute('update scriptData set time="'+ time +'" where inde = "' + entry['inde'] +'"')

fill_dialogues_times()
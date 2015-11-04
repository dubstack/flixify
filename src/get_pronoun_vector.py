import MySQLdb
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

stop = stopwords.words('english') + ["scene change"]
tokenizer = RegexpTokenizer(r"\w+")


def getData():
    db = MySQLdb.connect("10.5.18.68", "12CS30010", "dual12", "12CS30010")
    cursor = db.cursor()
    sql = "select * from scriptData"
    cursor.execute(sql)

    data = cursor.fetchall()
    return data


def get_all_chars(data):
    dic = {}
    for row in data:
        dic[row[1].lower()] = 1
    return dic


def get_tokenized_screenifo(chars, data):
    # data is in the following format
    # List of all sentences.
    # Each sentence is tuple of (char1, char2, list of tokenized words)

    ordered_char = []
    final_data = []
    print(chars)
    for row in data:
        if row[0] == "sceneInfo":
            scene_info = row[2].lower()
            scene_info = sent_tokenize(scene_info)
            for sent in scene_info:
                present_chars = []
                sent_tokens = tokenizer.tokenize(sent)
                sent_tokens = [token for token in sent_tokens if token not in stop]
                for token in sent_tokens:
                    if chars.has_key(token):
                        present_chars.append(token)
                present_chars.extend(ordered_char)
                new_ordered_char = []
                for l in present_chars:
                    if l not in new_ordered_char:
                        new_ordered_char.append(l)
                ordered_char = new_ordered_char
                
                final_data.append((sent, ordered_char))

    return final_data


def main():
    data = getData()
    
    chars = get_all_chars(data)

    tokenized_screeninfo = get_tokenized_screenifo(chars, data)
    print(tokenized_screeninfo[0:10])
    return tokenized_screeninfo

main()

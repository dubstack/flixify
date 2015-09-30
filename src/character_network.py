import MySQLdb
import nltk 
import operator
import json
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


stop = stopwords.words('english') + ["scene change"]
tokenizer = RegexpTokenizer(r"\w+")

def getData():
	db = MySQLdb.connect("10.5.18.68","12CS30010","dual12","12CS30010")
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

	final_data = []
	last_char1 = ""
	last_char2 = "" 
	for row in data:
		if row[0] == "sceneInfo":
			scene_info = row[2].lower()
			scene_info = sent_tokenize(scene_info)
			for sent in scene_info:
				present_chars = []
				sent_tokens = tokenizer.tokenize(sent)
				sent_tokens = [token for token in sent_tokens if token not in stop]
				for token in sent_tokens:
					if chars.has_key(token) :
						present_chars.append(token)
				sent_tokens = [token for token in sent_tokens if token not in present_chars]
				if len(present_chars) == 0:
					if last_char1 != "":
						final_data.append((last_char1,last_char2,sent_tokens))
				elif len(present_chars) == 1:
					if last_char1 != "":
						final_data.append((present_chars[0],last_char1,sent_tokens))
						last_char2 = last_char1
						last_char1 = present_chars[0] 
				else:
					final_data.append((present_chars[0],present_chars[1],sent_tokens))
					last_char1 = present_chars[0]
					last_char2 = present_chars[1]
	return final_data

def get_character_network(chars, data):
	scene_split_data = [[] for i in range(int(data[-1][3]))]
	dic = {}
	for row in data:
		scene_split_data[int(row[3])-1].append(row)

	for scene in scene_split_data:
		list1 = []
		speakers = []
		for row in scene:
			if row[0] == "dialogue":
				speakers.append(row[1].lower())
				list1.append(row[1].lower())
		speakers = set(speakers)
		for row in scene:
			info = row[2].lower()
			words = info.split()
			for word in words:
				if chars.has_key(word):
					list1.append(word)
		set1 = set(list1)
		tot_num = len(set1)
		for l in speakers:
			if l not in dic:
				dic[l] = {}
			for m in set1:
				if m not in dic[l]:
					dic[l][m] = 0.0
				dic[l][m] += 1.0/tot_num
	ans = {}
	for (key,x) in dic.items():
		ans[key] = sorted(x.items(), reverse=True, key=operator.itemgetter(1))
	return ans


def main():
	data = getData()
	chars = get_all_chars(data)
	# tokenized_screeninfo =  get_tokenized_screenifo(chars,data)
	# print tokenized_screeninfo
	ans = get_character_network(chars, data)
	with open("file.json","w+") as f:
		json.dump(ans,f)

if __name__ == '__main__':
	main()
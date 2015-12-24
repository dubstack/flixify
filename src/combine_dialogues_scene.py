from category_scores import *
import json

def  get_relations_dialogues():
	with open('speaker_speaker_words.json') as data_file:
		data = json.load(data_file)
	# print data["commodus"]["maximus"]
	# print data["maximus"]["commodus"]

	return data

def get_characters_dialogues():
	data = get_relations_dialogues()
	dic = {}
	for key,val in data.iteritems():
		li = []
		for key1,val1 in val.iteritems():
			for key2,val2 in val1.iteritems():
				li.append([key2,val2])
		dic[key] = li
	return dic

def get_relations_scenes():
	with open('relationships.json') as data_file:
		data = json.load(data_file)
	# print data["commodus,maximus"]
	return data

def get_characters_scenes():
	with open('profiles.json') as data_file:
		data = json.load(data_file)

	return data


def combine_relations(dic_relations_scenes, dic_relations_dialogues):
	dic = {}
	for key,val in dic_relations_scenes.iteritems():
		actor1,actor2 = key.split(",")
		dic[key] = {}
		for el in val:
			word,count = el
			dic[key][word] = count
		for key2,val2 in dic_relations_dialogues[actor2][actor1].iteritems():
			if key2 in dic[key]:
				dic[key][key2]+=val2
			else:
				dic[key][key2] = val2
		for key2,val2 in dic_relations_dialogues[actor1][actor2].iteritems():
			if key2 in dic[key]:
				dic[key][key2]+=val2
			else:
				dic[key][key2] = val2
	# print dic["commodus,maximus"]
	return dic

def combine_characters(dic_characters_scenes, dic_characters_dialogues):
	dic = {}
	for key,val in dic_characters_scenes.iteritems(): 
		dic[key] = {}
		for el in val:
			word,count = el
			dic[key][word] = count
		for el in dic_characters_dialogues[key]:
			if el[0] in dic[key]:
				dic[key][el[0]]+=el[1]
			else:
				dic[key][el[0]] = el[1]
	return dic

def get_scores(dic):
	new_dic = {}
	for key,val in dic.iteritems():
		print val
		new_dic[key] = get_results(val)
	return new_dic  

def write_results(dic_characters_scores, dic_relations_scores):
	json.dump(dic_characters_scores, open("character_scores.json", 'wb'))
	json.dump(dic_relations_scores, open("char_to_char_scores.json", 'wb'))


def main():
	dic_relations_dialogues = get_relations_dialogues()
	dic_relations_scenes = get_relations_scenes()
	dic_relations = combine_relations(dic_relations_scenes, dic_relations_dialogues)
	dic_characters_dialogues = get_characters_dialogues()
	dic_characters_scenes = get_characters_scenes()
	dic_characters = combine_characters(dic_characters_scenes, dic_characters_dialogues)
	print dic_characters
	dic_characters_scores = get_scores(dic_characters)
	dic_relations_scores = get_scores(dic_relations)
	print dic_characters_scores
	write_results(dic_characters_scores, dic_relations_scores)

if __name__ == '__main__':
	main()
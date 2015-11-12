from nltk.stem import *
stemmer = PorterStemmer()

def get_dic_categories():
	file_name = "LIWC2007.dic"
	lines = [line.rstrip('\n') for line in open(file_name)]
	lines = lines[1:]
	mapp = {}
	for line in lines:
		if line[0] == "%":
			break
		else:
			vals = line.split()
			mapp[vals[0]] = vals[1]
	lines = lines[65:]
	dic_categories = {}
	for line in lines:
		vals = line.split()
		cat = vals[0]
		vals = vals[1:]
		dic_categories[cat] = vals

	return dic_categories, mapp


def find_category_scores(dic_categories, mapp, words_dic):
	dic_out = {}
	for key,vals in mapp.iteritems():
		dic_out[key] = 0
	total_words = 0
	for word,val in words_dic.iteritems():
		total_words +=val
		if word in dic_categories:
			for cat in dic_categories[word]:
				dic_out[cat]+=val
		else:
			word_stem = stemmer.stem(word)
			if word_stem in dic_categories:
				for cat in dic_categories[word_stem]:
					dic_out[cat]+=val
			else:
				word_stem+="*"
				if word_stem in dic_categories:
					for cat in dic_categories[word_stem]:
						dic_out[cat]+=val

	dic_final = {}
	for key, vals in dic_out.iteritems():
		dic_final[mapp[key]] = (float(vals))/total_words
	return dic_final

def select_cats(dic_result):
	new_dic = {}
	for key,val in dic_result.iteritems():
		if key in ["negemo","posemo","anger","sad", "sexual"]:
			new_dic[key] = val
	return new_dic

def get_results(words_dic):
	dic_categories, mapp = get_dic_categories()
	dic_result = find_category_scores(dic_categories, mapp, words_dic)
	dic_result = select_cats(dic_result)
	return dic_result

def main():
	find_category_scores(words)
	find_category_scores(dic_categories, mapp, words_list)

if __name__ == '__main__':
	main()
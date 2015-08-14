def main():
	lines = [line.rstrip('\n') for line in open('../scripts/gladiator_transcript.txt')]
	lines=lines[2:]
	n_iter_ = 0
	intro=""
	while True:
		if len(lines[n_iter_]) != 0:
			if lines[n_iter_][0] == "*":
				n_iter_ += 1
				break
			else :
				intro += lines[n_iter_]
		n_iter_ += 1
	n_iter_ += 1
	openingScene = ""
	while True:
		if len(lines[n_iter_]) != 0:
			openingScene += lines[n_iter_]
		else :
			n_iter_ += 1
			break
		n_iter_ += 1
	openingScene = openingScene[27:]
	scenenum=0
	store = []
	lastSpeaker = ""
	while True :
		if len(lines[n_iter_].strip()) != 0 :
			if lines[n_iter_][0] == "[":
				lines[n_iter_] = lines[n_iter_][1:]
				sceneInfo = ""
				while True :
					lineLength = len(lines[n_iter_])
					if lineLength == 0:
						n_iter_ += 1
						break
					if lines[n_iter_][lineLength-1] == "]" :
						sceneInfo += lines[n_iter_][:-1]
						n_iter_ += 1
						break
					else :
						sceneInfo += lines[n_iter_]
						n_iter_ += 1
				if "scene" == sceneInfo.lower()[:5] :
					scenenum += 1
				store.append( {"type" : "sceneInfo","speaker" :lastSpeaker, "content" : sceneInfo ,"scenenum":str(scenenum)})
			elif lines[n_iter_].strip().isupper() :
				lastSpeaker = lines[n_iter_].strip().lower()
				n_iter_ += 1
			else :
				dialogue = ""
				flag = False
				while True :
					if lines[n_iter_].strip() == "- The End -" : 
						flag = True
						break
					if len(lines[n_iter_].strip()) != 0  and lines[n_iter_][0] != "[" :
						dialogue += lines[n_iter_]
						n_iter_ += 1
					else :
						break
				if flag :
					break
				store.append({"type":"dialogue","speaker" : lastSpeaker, "content" : dialogue ,"scenenum":str(scenenum)})
		else :
			n_iter_ += 1
	writeToDB(store)
if __name__ == '__main__':
	main()
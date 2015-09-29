def scripttolist(location):



def word2vec(word):



def Main():
	location=""
	words_sub1_sub2=scripttolist(location)
	categories=5

	numberofsubs=0
	sub={}
	index=0
	for I in scripttolist:
		sub[I[1]]=sub.get(I[1],-1)
		if sub[I[1]]==-1:
			sub[I[1]]=index
			index+=1
		sub[I[2]]=sub.get(I[2],-1)
		if sub[I[2]]==-1:
			sub[I[2]]=index
			index+=1

	numberofsubs=index
	matrix=[]
	for i in range(0,numberofsubs):
		X=[]
		for j in range(0,numberofsubs):
			Y=[]
			for k in range(0,categories):
				Y.append(0.0)
			X.append(Y)
		matrix.append(X)

	for I in scripttolist:
		score=[]
		for l in range(0,categories):
			score.append(0.0)
		for word in I[0]:
			temp=word2vec(word)
			for l in range(0,categories):
				score[l]+=temp[l]
		for l in range(0,categories):
			matrix[sub[I[1]]][sub[I[2]]][l]=score[l]

	






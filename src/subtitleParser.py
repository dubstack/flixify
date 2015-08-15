import sys
if __name__ == "__main__":
	f = open('../subtitles/gladiator.srt', 'r')
	i = 1
	time = ""
	text = ""
	result = []
	flag = 0
	all = f.read().split("\n")
	#print all
	for s in all:
		# print s
		s = s[:-1]
		if  i ==10:
			break
		if flag==0:
			flag=1
		elif flag == 1:
			x = s.split(',')
			time = x[0]
			flag = 2
		elif flag == 2:
			print s
			if s!=str(i+1):
				text = text +" " + s
			else:
				print s
				i = i + 1
				val = {}
				val['Time'] = time
				val['Text'] = text
				result.append(val)
				text = ""
				flag = 1


	print result




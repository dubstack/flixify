import os
def dependency_parse(s):
	workfile = open("/home/gaurav/stanford-parser-full-2014-10-31/input.txt",'w+')
	workfile.write(s)
	workfile.close()
	os.system('~/stanford-parser-full-2014-10-31/lexparser.sh /home/gaurav/stanford-parser-full-2014-10-31/input.txt > output.txt')
	infile = open('output.txt')
	subjects = []
	objects = []
	roots = []
	for line in infile:
		if line[0:5] == "nsubj":
			x = line.split("(")
			y = x[1].split(",")
			p1 = y[0].split("-")[0]
			p2 = y[1].split("-")[0][1:]
			subjects.append((p1,p2))
		elif line[0:4] == "root":
			x = line.split("(")
			y = x[1].split(",")
			p1 = y[0].split("-")[0]
			p2 = y[1].split("-")[0][1:]
			roots.append(p2)
		elif line[0:4] == "dobj":
			x = line.split("(")
			y = x[1].split(",")
			p1 = y[0].split("-")[0]
			p2 = y[1].split("-")[0][1:]
			objects.append((p1,p2))
	triplets = []
	for sub in subjects:
		for obj in objects:
			if sub[0] == obj[0]:
				triplets.append((sub[1],sub[0],obj[1]))
	print triplets

if __name__ == '__main__':
	dependency_parse("He killed him.")
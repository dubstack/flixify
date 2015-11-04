import os

def dependency_parse_relations(s, chars):
    #returns list of [verb, subject, object]
    if len(chars) < 2:
        return []
    pronouns = ["he", "she", "himself", "herself", "him", "her"]
    workfile = open("/Users/arkanath/Stanford-Parser/stanford-parser-full-2014-10-31/input.txt", 'w+')
    workfile.write(s)
    workfile.close()
    os.system(
        '/Users/arkanath/Stanford-Parser/stanford-parser-full-2014-10-31/lexparser.sh /Users/arkanath/Stanford-Parser/stanford-parser-full-2014-10-31/input.txt > output.txt')
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
            subjects.append((p1, p2))
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
            objects.append((p1, p2))
    triplets = []
    for sub in subjects:
        for obj in objects:
            if sub[0] == obj[0]:
                triplets.append((sub[1], sub[0], obj[1]))
    ans = []
    for trip in triplets:
        subj = trip[0]
        obj = trip[2]
        vb = trip[1]
        flag = 0
        if subj not in chars and subj not in pronouns:
            continue
        if subj not in chars:
            subj = chars[0]
            flag = 1
        if obj not in chars and obj not in pronouns:
            continue
        if obj not in chars:
            obj = chars[flag]
        ans.append([vb,subj,obj])
    return ans

def dependency_parse_profile(s, chars):
    #returns list of [verb, subject]
    if len(chars) < 1:
        return []
    pronouns = ["he", "she", "himself", "herself", "him", "her"]
    workfile = open("/Users/arkanath/Stanford-Parser/stanford-parser-full-2014-10-31/input.txt", 'w+')
    workfile.write(s)
    workfile.close()
    os.system(
        '/Users/arkanath/Stanford-Parser/stanford-parser-full-2014-10-31/lexparser.sh /Users/arkanath/Stanford-Parser/stanford-parser-full-2014-10-31/input.txt > output.txt')
    infile = open('output.txt')
    subjects = []
    for line in infile:
        if line[0:5] == "nsubj":
            x = line.split("(")
            y = x[1].split(",")
            p1 = y[0].split("-")[0]
            p2 = y[1].split("-")[0][1:]
            subjects.append((p1, p2))
    ans = []
    for trip in subjects:
        vb = trip[0]
        subj = trip[1]
        if subj not in chars and subj not in pronouns:
            continue
        if subj not in chars:
            subj = chars[0]
        ans.append([vb,subj])
    return ans
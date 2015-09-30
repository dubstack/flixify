import os
import json 

class Myjson(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        dic = range(10,671, 10) + ["Final"]
        for num in dic:# in os.listdir(self.dirname):
            filename = "output/out"+str(num)+".json"
            # print filename
            with open(filename) as f:
                yield json.load(f)



def get_temp():
    ret = {}
    i = 0
    for j in Myjson("output"):
        for pair in j:
            if pair not in ret:
                ret[pair] = {}
            ret[pair][i] = (j[pair][1] - j[pair][0])
        i+=1
    sz = i
    rett = {}
    for pair in ret:
        las = 0
        for i in range(0,sz):
            if i in ret[pair]:
                las = ret[pair][i]
            if pair not in rett:
                rett[pair] = []
            rett[pair].append(las)

    return rett

with open("temporal", "w") as f:
    json.dump(get_temp(), f)

# res =  get_temp()
# for key in res:
#     print len(res[key])

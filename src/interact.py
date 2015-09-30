import json
lis = []
with open("output/outFinal.json") as f:
    c = json.load(f)
for pair in c:
    lis.append((c[pair][0]+c[pair][1], pair))

ans = reversed(sorted(lis))
for item in ans:
    print item

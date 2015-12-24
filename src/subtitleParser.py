__author__ = '9310gaurav'

def get_subtitle_list_from_file(filename):
    f = open(filename, 'r')
    i = 1
    time = ""
    text = ""
    result = []
    flag = 0
    all = f.read().split("\n")
    for s in all:
        if flag == 0:
            if s == str(i):
                flag = 1
            continue
        if flag == 1:
            x = s.split(',')
            time = x[0]
            flag = 2
            continue
        if flag == 2:
            if len(s)==0:
                if len(text)!=0:
                    val = {}
                    val['time'] = time
                    val['text'] = text
                    result.append(val)
                text = ""
                flag = 0
                i = i + 1
                continue

            if s[0]=='-':
                if len(text)!=0:
                    val = {}
                    val['time'] = time
                    val['text'] = text
                    result.append(val)
                if s[-1]=='.':
                    s = s[:-1]
                text = s[2:]
            else:
                text = text + " " + s
    return result
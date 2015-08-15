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
        s = s[:-1]
        if flag == 0:
            flag = 1
        elif flag == 1:
            x = s.split(',')
            time = x[0]
            flag = 2
        elif flag == 2:
            if s != str(i + 1):
                text = text + " " + s
            else:
                i = i + 1
                val = {}
                val['time'] = time
                val['text'] = text
                result.append(val)
                text = ""
                flag = 1
    return result
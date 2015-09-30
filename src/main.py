import tokenize_narrative
import get_vector
import json

memo = {}

def Main():
    scripttolist = tokenize_narrative.main()
    categories = 2
    # get_vector.init_wn_synsets()

    numberofsubs = 0
    sub = {}
    index = 0
    for I in scripttolist:
        sub[I[1]] = sub.get(I[1], -1)
        if sub[I[1]] == -1:
            sub[I[1]] = index
            index += 1
        sub[I[2]] = sub.get(I[2], -1)
        if sub[I[2]] == -1:
            sub[I[2]] = index
            index += 1

    numberofsubs = index
    matrix = {}
    # for i in range(0, numberofsubs):
    #     X = []
    #     for j in range(0, numberofsubs):
    #         Y = []
    #         for k in range(0, categories):
    #             Y.append(0.0)
    #         X.append(Y)
    #     matrix.append(X)

    vectorable = 0
    nonvectorable = 0
    done = 0
    ndone = 0
    for I in scripttolist:
        done+=1
        print done,"done"
        if(done>=ndone+10):
            ndone=done
            # break
            with open("output/out"+str(ndone)+".json","w+") as f:
                json.dump(matrix,f)
                print "Saved."
        score = get_vector.get_vector(I[0])
        if (I[1]+","+I[2]) not in matrix:
            matrix[(I[1]+","+I[2])] = [0.0,0.0]
        # print matrix[sub[I[1]]][sub[I[2]]]
        for l in range(0, categories):
            matrix[(I[1]+","+I[2])][l] += score[l]

    print matrix
    with open("out.json","w+") as f:
        json.dump(matrix,f)
    # print matrix[sub["maximus"]][sub["commodus"]]


if __name__ == "__main__":
    Main()







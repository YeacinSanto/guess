def getData(file):
    try:
        with open(file) as infile:
            line = infile.readline().strip()
            linelist = []
            while line != "":
                tmplist = line.split(";")
                linelist.append(tmplist)
                line = infile.readline().strip()
        return linelist

    except Exception as a:
        print(a)
        exit()

def question(file):
    try:
        with open(file,"r") as infile:
            line = infile.readline().strip()
            linelist = []
            while line != "":
                tmplist = line.split(" = ")
                linelist.append(tmplist)
                line = infile.readline().strip()
        return linelist
    except Exception as a:
        print(a)
        exit()
def manipulation():
    char = getData("characters.txt")
    ques = question("question2.txt")
    result = []
    step = 1
    for i in range(len(ques)):
        index = char[0].index(ques[i][0])
        for j in range(1, len(char)):
            if ques[i][1] == char[j][index]:
                if step == 1:
                    result.append(char[j])
                if char[j] in result:
                    print(char[j])
        print()
        step += 1

manipulation()


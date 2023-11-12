def getChar(file):
    with open(file,"r") as infile:
        line = infile.readline().strip()
        linelist = []
        while line != "":
            tmplist = line.split(";")
            linelist.append(tmplist)
            line = infile.readline().strip()
    return linelist

def getQues(file):
    with open(file,"r") as infile:
        line = infile.readline().strip()
        linelist = []
        while line != "":
            tmplist = line.split(" = ")
            linelist.append(tmplist)
            line = infile.readline().strip()
    return linelist

def main():
    char = getChar("characters.txt")
    ques = getQues("question1.txt")
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

if __name__ == '__main__':
    main()



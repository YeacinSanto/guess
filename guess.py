

def getData(file):
    with open(file,"r") as infile:
        line = infile.readline().strip()
        lineList = []
        while line != "":
            tmplist = line.strip().split(";")
            lineList.append(tmplist)
            line = infile.readline().strip()
    return lineList


def question(file):
    with open(file,"r") as infile:
        line = infile.readline().strip()
        linelist = []
        while line != "":
            tmplist = line.split(" = ")
            linelist.append(tmplist)
            line = infile.readline().strip()
    return linelist


def matching(character,question):
    sort = []
    for i in range(len(character)):
        if character[i][2] == question[0][1] and character[i][3] == question[
            1][1] \
                and \
                character[i][4] == question[2][1]:
            sort.append(character[i])
    return sort


def main():
    data = getData("characters.txt")
    ques = question("question1.txt")
    match = matching(data,ques)

    k = 0
    while k<= len(match):
        done = False
        k += 1
    print(match)
    if k > 1:
        print("Yo")
    else:
        print("Vo")
    """for i in range(len(match)):
        print(match[i])"""


if __name__ == '__main__':
    main()


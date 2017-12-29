def name_score(filename):
    list1 = []
    list2 = []
    list3 = []
    myval = 0
    final = 0
    with open(filename) as file:
        for line in file:
            list1 = line.strip().split(",")
    list1.sort()        
    for names in range(0, len(list1)):
        for letters in range(0, len(list1[names])):
            myval += ord(list1[names][letters]) - 64
        list2.append(myval)

    for pos in range(0, len(list1)):
        list3.append(list1.index(list1[pos]) + 1)

    for products in range(0, len(list1)):
        pro = list2[products] * list3[products]
        final += pro

    print final

    file.close()


if __name__ == '__main__':
    name_score("names.txt")

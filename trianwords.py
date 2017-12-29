def triangles(num):
    list1 = []
    for i in range(1, num+1):
        list1.append(0.5*i*(i+1))
    return list1
    
def get_score(name):
    return sum([ord(letter)-64 for letter in name])

def wordsConverter(filein):
    list2 = []
    list3 = []
    count = 0
    with open(filein) as file:
        for lines in file:
            list1 = lines.strip().split(",")
    list2 = triangles(len(list1))
            
    for names in range(0,len(list1)):
        list3.append(get_score(list1[names]))
        for i in range(0, len(list2)):
            if list3[names] == list2[i]:
                count = count + 1
        
    print count 
    
if __name__ == '__main__':
    wordsConverter("words.txt")
 

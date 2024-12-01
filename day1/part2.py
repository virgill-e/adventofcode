import math

def create_lists():
    list1 = []
    list2 = []

    fichier = open("day1/input.txt", "r")
    for line in fichier:
        split = line.split()
        list1.append(int(split[0]))
        list2.append(int(split[1]))
    fichier.close()
    return list1, list2





list1, list2 = create_lists()
distance = 0
nbNbr = len(list1)
for i in range(nbNbr):
    nbr1=list1[i]
    nbr2=list2.count(nbr1)
    distance+=nbr1*nbr2
print(distance)



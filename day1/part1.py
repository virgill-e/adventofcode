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
nbNbr = max(len(list1), len(list2))
for i in range(nbNbr):
    min1=min(list1)
    min2=min(list2)
    distance += abs(min1-min2)
    list1.remove(min1)
    list2.remove(min2)
print(distance)



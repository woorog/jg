import sys

a=int(sys.stdin.readline())


def pivo(a):

    point=2
    while len(listpivo)<=a:
        nextpivo=listpivo[point]+listpivo[point-1]
        listpivo.append(nextpivo)
        point+=1

listpivo=[0,1,1]
pivo(a)

print(listpivo[a])
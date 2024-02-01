import sys

a=int(sys.stdin.readline())



listpivo=[0,1]

pivo=[]

for _ in range(a):
    nextpivo=(listpivo[0]+listpivo[1])%1000000007
    temp=listpivo[1]
    listpivo[0]=temp
    listpivo[1]=nextpivo
    pivo.append(nextpivo)


print(pivo)
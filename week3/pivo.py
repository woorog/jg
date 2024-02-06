import sys

#
# def fibonacci(n):
#     if (n == 0) :
#         print("0")
#         return 0
#     elif n == 1:
#         print("1")
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


pivo=[[0]*2 for _ in range(41)]

pivo[0]=[1,0]
pivo[1]=[0,1]
pivo[2]=[1,1]
pivo[3]=[1,2]


for i in range(4,41):
    pivo[i][0]=pivo[i-1][0]+pivo[i-2][0]
    pivo[i][1]=pivo[i-1][1]+pivo[i-2][1]
tc=int(sys.stdin.readline())

for _ in range(tc):
    n=int(sys.stdin.readline())
    for i in range(2):
        print(pivo[n][i],end=' ')
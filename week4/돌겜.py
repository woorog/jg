import sys

a=int(sys.stdin.readline())

if a==2:
    print("CY")
elif a==1 or a==3 or a==4 or a==5 or a==6:
    print("SK")
else:
    a=a%7
    if a==0 or a==2:
        print("CY")
    else:
        print("SK")
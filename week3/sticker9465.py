import sys

tc=int(sys.stdin.readline())
a=[]
for _ in range(tc):
    num=int(sys.stdin.readline())
    x=list(map(int,sys.stdin.readline().split()))
    y=list(map(int,sys.stdin.readline().split()))
    x.append(0)
    x.append(0)
    y.append(0)
    y.append(0)


    dpx=[0] * (num + 2)
    dpy=[0] * (num + 2)
    dpx[0]=x[0]
    dpy[0]=y[0]

    for i in range(num):
        if dpx[i]+x[i+2]>dpx[i+2]:
            dpx[i+2]=dpx[i]+x[i+2]
        if dpx[i]+y[i+1]>dpy[i+1]:
            dpy[i+1]=dpx[i]+y[i+1]
        if  dpx[i]+y[i+2]>dpy[i+2]:
            dpy[i+2]=dpx[i]+y[i+2]

        if  dpy[i]+y[i+2]>dpy[i+2]:
            dpy[i+2]=dpy[i]+y[i+2]
        if  dpy[i]+x[i+1]>dpx[i+1]:
            dpx[i+1]=dpy[i]+x[i+1]
        if  dpy[i]+x[i+2]>dpx[i+2]:
            dpx[i+2]=dpy[i]+x[i+2]


    a.append(max(max(dpx),max(dpy)))

for k in range(tc):
    print(a[k])

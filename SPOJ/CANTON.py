from math import sqrt
def result(n):
    d = (-1 + sqrt(1 + 8*n)) // 2
    e = n - (d*(d+1))//2

    if e<=1:
        v1,v2 = d+e,1
    else:
        v1,v2 = d+2-e,e

    v1 = int(v1)
    v2 = int(v2)

    if d%2==0:
        print("TERM "+str(n)+" IS "+str(v1)+"/"+str(v2))
    else:
        print("TERM "+str(n)+" IS "+str(v2)+"/"+str(v1))

for _ in range(int(input())):
    n = int(input())
    result(n)

from math import sqrt
for _ in range(int(input())):
    n, m = map(int,input().split())
    if m==1:
        if sqrt(n)%1==0:
            print(int(sqrt(n)))
        else:
            print(-1)
    elif n==0:
        print(0)
    else:
        limit = 1000000
        for i in range(limit):
            if sqrt((i*m + n))%1==0:
                print(int(sqrt(i*m + n)))
                break
        else:
            print(-1)

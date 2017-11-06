import math
for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = []
    if n==1 and m!=0:
        print(-1)
    elif n==1 and m==0:
        print(0)
    elif n%2==0:
        a = math.sqrt(m*m)
        if a==0:
            arr=[0]*(n)
        else:
            if a%1==0:
                a = int(a)
            else:
                a = round(a, 6)
            arr = [a]*(n//2)
            arr += [-a]*(n//2)
        print(*arr, sep=" ")
    else:
        k = (m*m*n)/(n-1)
        a = math.sqrt(k)
        if a==0:
            arr = [0]*(n)
        else:
            if a%1==0:
                a = int(a)
            else:
                a = round(a, 6)
            arr = [a]*((n-1)//2)
            arr += [-a]*((n-1)//2)
            arr += [0]
        print(*arr, sep=" ")
        

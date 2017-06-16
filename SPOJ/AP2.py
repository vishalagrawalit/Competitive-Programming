for _ in range(int(input())):
    a, b, c = map(int,input().split())
    n = (c * 2)//(a+b)
    print(n)
    diff = (b-a)//(n-5)
    first = (a-2*diff)
    arr = []
    for i in range(1,n+1):
        arr.append(first + (i-1)*diff)
    print(*arr,sep=" ")

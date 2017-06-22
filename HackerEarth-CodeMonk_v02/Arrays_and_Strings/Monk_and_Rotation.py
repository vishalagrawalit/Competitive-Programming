for _ in range(int(input())):
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    if k%n==0:
        print(*arr,sep=" ")
    else:
        x = k%n
        print(*(arr[n-x:] + arr[:n-x]),sep=" ")

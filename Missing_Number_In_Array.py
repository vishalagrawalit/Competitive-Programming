for _ in range(int(input())):
    n = int(input())

    tot = (n*(n+1))//2

    arr = list(map(int,input().split()))

    print(tot - sum(arr))

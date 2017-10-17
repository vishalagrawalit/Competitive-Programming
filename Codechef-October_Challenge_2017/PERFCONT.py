for _ in range(int(input())):
    m, n = map(int, input().split())
    arr = list(map(int, input().split()))
    cake, hard = 0, 0
    for i in range(m):
        if arr[i]>=n//2:
            cake+=1
        elif arr[i]<=n//10:
            hard+=1
    if cake==1 and hard==2:
        print("yes")
    else:
        print("no")

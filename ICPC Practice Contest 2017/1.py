for _ in range(int(input())):
    t = int(input())
    arr = list(map(int, input().split()))
    lis = [0]*101
    for i in range(t):
        lis[arr[i]]+=1
    for i in range(1, 101):
        if lis[i]==1:
            print(i)
            break

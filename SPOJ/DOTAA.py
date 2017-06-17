for _ in range(int(input())):
    n, m, D = map(int,input().split())
    arr = []
    for _ in range(n):
        h = int(input())
        arr.append(h)
    arr.sort()
    count = 0
    for i in range(n-1,-1,-1):
        if arr[i]>D:
            count+=1
        else:
            print("NO")
            break
        if count==m:
            print("YES")
            break

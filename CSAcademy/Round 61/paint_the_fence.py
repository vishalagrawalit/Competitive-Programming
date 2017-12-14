n, m = map(int, input().split())

arr = [0]*(n+1)
arr[0] = -1
check = []

for i in range(m):
    l, r = map(int, input().split())
    check.append((l, r))
    for j in range(l, r+1):
        arr[j]+=1
        

for i in range(m):
    ans = 0
    for j in range(check[i][0], check[i][1]+1):
        if arr[j]==1:
            ans+=1
    print(ans+arr.count(0))

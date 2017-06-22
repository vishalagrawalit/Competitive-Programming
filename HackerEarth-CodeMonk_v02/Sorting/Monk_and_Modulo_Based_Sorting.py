n, k = map(int,input().split())
arr = list(map(int,input().split()))

for i in range(n):
    arr[i] = (arr[i],arr[i]%k)

ans = sorted(arr, key = lambda x:x[1])

for i in range(n):
    arr[i] = ans[i][0]

print(*arr, sep=" ")

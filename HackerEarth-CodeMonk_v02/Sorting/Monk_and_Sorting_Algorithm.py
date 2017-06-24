n = int(input())
arr = list(map(str, input().split()))

j = 0
while j>=0:
    lis = []
    for i in range(n):
        lis.append((int(arr[i]), int(arr[i][len(arr[i])-5*i: len(arr[i])-i])))
    ans = sorted(lis, key = lambda x:x[1])

    for k in range(n):
        ans[k] = ans[k][0]
    print(*ans,sep=" ")
    j+=1

def search(pre, n, k):
    ans, left, right = -1, 1, n
 
    while (left <= right):
 
        mid = (left + right)//2
  
        for i in range(mid,n+1):
            if (pre[i] - pre[i - mid] > k):
                i = i-1
                break
        i = i+1
        if (i == n+1):
            left = mid + 1
            ans = mid
        else:
            right = mid -1
  
    return ans

n,k = map(int,input().split())
arr = list(map(int,input().split()))
add = [0]*(n+1)
for i in range(n):
    add[i+1] = add[i] + arr[i]
print(search(add, n, k))

def upper_bound(A, target, length):
    lo, high = 0, length + 1
    if A[length]==target:
        return length
    while lo < high:
        mid = (high + lo) >> 1
        if A[mid]<=target:
            lo = mid+1
        else:
            high = mid
    return lo
n, q = map(int,input().split())
arr,add = [],[0]
for i in range(n):
    l, r = map(int,input().split())
    arr.append((l,r))
    add.append(add[i]+(r-l+1))
#print(add)
for _ in range(q):
    y = int(input())
    x = upper_bound(add,y,n)
    #print(x)
    index = y - add[x-1] - 1
    #print(index)
    print(arr[x-1][0]+index)

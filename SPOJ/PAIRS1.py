def binarySearch(arr, l, r, x):
    while l <= r:
        mid = (l + r)//2;
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return False

n, k = map(int,input().split())
arr = list(map(int,input().split()))


arr.sort()
count = 0

for i in range(n):
    if binarySearch(arr, 0, n-1, arr[i]+k) :
        count+=1
print(count)

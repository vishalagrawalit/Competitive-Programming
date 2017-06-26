def binarysearch(arr, l, r, x):
    while l <= r:
        mid = (l + r)//2;
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return False

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    p = int(input())
    arr.sort()
    flag = 0

    for i in range(n-2):
        for j in range(i+1,n-1):
            if binarysearch(arr, j+1, n-1, p-arr[i]-arr[j]):
                flag = 1
                break
        if flag==1:
            print("YES")
            break
    if flag==0:
        print("NO")

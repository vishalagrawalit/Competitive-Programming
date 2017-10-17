def binarySearch(arr, l, r, x):

    while l <= r:
        mid = l + (r - l)//2;

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            l = mid + 1

        else:
            r = mid - 1

    return -1

MAX = 2*(10**5)
for _ in range(int(input())):
    s, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(MAX):
        if binarySearch(arr, 0, s-1, i)==-1:
            if k==0:
                print(i)
                break
            else:
                k-=1

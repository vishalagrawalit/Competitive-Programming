def binarysearch(arr, length, x):
    count = 0
    if length<1:
        return count
    low,high = 0, length-1
    while low < high:
        add = arr[low]+arr[high]
        if add == x:
            count+=1
            low+=1
            high-=1
        elif add > x:
            high-=1
        else:
            low+=1
    return count

for _ in range(int(input())):
    n, num = map(int,input().split())
    arr = list(map(int,input().split()))

    arr.sort()
    count = 0

    print(binarysearch(arr, n, num))

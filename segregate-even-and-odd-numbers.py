from bisect import insort

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    left, right = 0, n-1
    even, odd= [], []

    while left<=right:
        if arr[left]%2==0:
            insort(even, arr[left])
            left+=1
            
        elif arr[right]%2==1:
            insort(odd, arr[right])
            right-=1
            
        else:
            arr[left],arr[right]=arr[right],arr[left]
            insort(even, arr[left])
            insort(odd, arr[right])
            left+=1
            right-=1

    print(*(even+odd),sep=" ")

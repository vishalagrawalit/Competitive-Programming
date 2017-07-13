from bisect import bisect

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    flag = 0
    new = []
    for i in range(n):
        index = bisect(new, arr[i])
        new.append(arr[i])

        if index!=i and flag==0:
            flag = 1
            left = index
            
        elif index==i and flag==1:
            flag = 2

        elif index==i and flag==2:
            flag = -1
            right = i

    print(left, right)
            

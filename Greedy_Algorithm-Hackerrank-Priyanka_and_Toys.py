n = int(input())
arr = list(map(int,input().split()))
arr.sort()
i,count = 1,1
first,last = arr[0],arr[0]+5
while i<n:
    if arr[i] not in range(first,last):
        count+=1
        first = arr[i]
        last = arr[i]+5
    i+=1
print(count)

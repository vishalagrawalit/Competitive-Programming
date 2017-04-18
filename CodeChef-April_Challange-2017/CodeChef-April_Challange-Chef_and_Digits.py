for _ in range(int(input())):
    ranges = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    count=0
    for i in range(ranges[0],ranges[1]+1):
        integers = list(str(i))
        for j in range(10):
            if integers.count(str(j))==arr[j]:
                count+=1
                break
    print(ranges[1]-ranges[0]-count+1)

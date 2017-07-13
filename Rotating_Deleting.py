for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    i=1

    while n>1:
        arr.insert(0, arr[-1])
        arr.pop(-1)

        if len(arr)>i:
            arr.pop(-i)
        else:
            arr.pop(0)
        
        i+=1
        n-=1
        
    print(arr[0])

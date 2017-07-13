for _ in range(int(input())):
    m, n = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    
    arr2 = list(set(arr1 + arr2))
    
    print(*arr2, sep=" ")

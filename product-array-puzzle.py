for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    
    left = [1]
    for i in range(1, n):
        product = left[i-1]*arr[i-1]
        left.append(product)

    right = [1]
    for i in range(n-1,0,-1):
        product = right[0]*arr[i]
        right.insert(0, product)

    for i in range(n):
        left[i] *= right[i]
    
    print(*left, sep=" ")

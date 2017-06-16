for _ in range(int(input())):
    arr = list(map(int,input().split()))
    for _ in range(arr[1]):
        new = list(map(int,input().split()))
    if arr[0]%2==0:
        print("yes")
    else:
        print("no")

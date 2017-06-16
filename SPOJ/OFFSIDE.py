m, n = map(int,input().split())
while m!=0 and n!=0:
    arr1 = list(map(int,input().split()))
    arr1.sort()
    arr2 = list(map(int,input().split()))
    arr2.sort()

    if arr1[0]<arr2[1]:
        print("Y")
    else:
        print("N")

    m, n = map(int,input().split())

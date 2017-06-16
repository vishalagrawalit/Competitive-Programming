n = int(input())

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

mini1, mini2 = min(arr1), min(arr2)
if arr1.index(mini1)!=arr2.index(mini2):
    print(mini1 + mini2)

else:
    arr1[arr1.index(mini1)]=10000000
    arr2[arr2.index(mini2)]=10000000

    if min(arr1) > min(arr2):
        print(mini1 + min(arr2))
    else:
        print(mini2 + min(arr1))

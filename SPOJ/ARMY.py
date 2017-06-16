for _ in range(int(input())):
    n = input()
    number = list(map(int,input().split()))
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))

    if max(arr1) >= max(arr2):
        print("Godzilla")
    else:
        print("MechaGodzilla")

arr = list(map(int,input().split()))
while arr != [0]*3:
    if arr[1]-arr[0] == arr[2]-arr[1]:
        print("AP " + str(2*arr[2]-arr[1]))
    else:
        print("GP " + str(arr[2]*arr[2]//arr[1]))
    arr = list(map(int,input().split()))

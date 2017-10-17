for _ in range(int(input())):
    n = int(input())
    quality, number = [], []
    for i in range(n):
        arr = list(map(int, input().split()))
        quality.append(arr[1:].sort())
        number.append(arr[0])

    print(quality)
    print(number)

    if abs(arr[n-1][0]-arr[n-2][number[n-2]-1]) > abs(arr[n-2][0]-arr[n-1][number[n-1]-1]):
        ans = abs(arr[n-1][0]-arr[n-2][number[n-2]-1]) * i
        maxi = 0
        mini = 1
    else:
        ans = abs(arr[n-2][0]-arr[n-1][number[n-1]-1]) * i
        mini = 0
        maxi = 1


    for i in range(n-2, 0, -1):
        if maxi==0:
            ans += abs(arr[i-1][0]-arr[i][number[i]-1]) * i
            mini = 0
            maxi = 1
        elif mini==0:
            ans += abs(arr[i][0]-arr[i-1][number[i-1]-1]) * i
            maxi = 0
            mini = 1

    print(ans)

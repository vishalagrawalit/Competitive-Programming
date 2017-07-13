for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    maxi = arr[0]
    answer = arr[0]

    for i in range(1,n):
        maxi = max(arr[i], maxi+arr[i])
        answer = max(answer, maxi)

    print(answer)

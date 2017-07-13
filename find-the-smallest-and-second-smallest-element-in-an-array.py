# In O(n) time complexity

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    arr = list(set(arr))

    if len(arr)==1:
        print(-1)
    else:
        mini1, mini2 = arr[0], arr[1]
        for i in range(2,len(arr)):
            if mini1 == min(mini1, mini2, arr[i]):
                mini2 = min(mini2, arr[i])

            elif mini2 == min(mini1, mini2, arr[i]):
                mini1 = min(mini1, arr[i])

            else:
                mini1 = min(mini1, mini2)
                mini2 = arr[i]

        print(min(mini1, mini2),max(mini1, mini2))

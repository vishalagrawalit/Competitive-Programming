test = int(input())
while test!=-1:
    add,arr = 0,[]
    for _ in range(test):
        n = int(input())
        arr.append(n)
        add += n
    if add%test==0:
        ans = 0
        for i in range(test):
            if arr[i] < add//test:
                ans += add//test - arr[i]
        print(ans)
    else:
        print(-1)
    test = int(input())

for _ in range(int(input())):
    t = int(input())
    arr = list(map(int, input().split()))
    count = 0
    for i in range(t):
        add , pro = 0, 1
        for j in range(i, t):
            add+=arr[j]
            pro*=arr[j]
            if add==pro:
                count+=1
    print(count)

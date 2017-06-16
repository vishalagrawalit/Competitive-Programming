for _ in range(int(input())):
    arr = list(map(int,input().split()))
    u,v = arr[0],arr[1]

    passed_rank = ((u+v) * (1 + u + v))//2

    print(passed_rank + 1 + u)

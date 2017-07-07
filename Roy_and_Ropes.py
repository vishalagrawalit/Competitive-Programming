for _ in range(int(input())):
    length = int(input())

    upper = list(map(int,input().split()))
    lower = list(map(int,input().split()))

    maxi = -1

    for i in range(2*len(upper)):
        if i>=len(upper):
            time = lower[i]+ i%len(upper) + 1
        else:
            time = upper[i]+ i + 1

        if time>maxi:
            maxi = time

    print(max(maxi, length))

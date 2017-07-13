from collections import Counter

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    li = Counter(arr)

    for i in range(n):
        if li[i]>n//2:
            print(i)
            break
    else:
        print("NO Majority Element")

from collections import Counter

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    li = Counter(arr)

    for i in range(1001):
        if li[i]%2==1:
            print(i)
            break

#Use bitwise XOR.

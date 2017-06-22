from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    c = Counter(a)
    c = list(c.values())
    c.sort()
    if (c[-1]-c[0]):
        print(c[-1]-c[0])
        continue
    print(-1)

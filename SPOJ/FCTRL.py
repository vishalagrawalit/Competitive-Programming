from math import floor,log
for _ in range(int(input())):
    n = int(input())
    x = floor(log(n, 5))
    add = 0
    for i in range(1,x+1):
        add+=(n//(5**i))
    print(add)

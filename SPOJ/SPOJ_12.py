for _ in range(int(input())):
    print("")
    n = int(input())
    add = 0
    for i in range(n):
        candies = int(input())
        add += candies
        if add >= n:
            add %= n
            
    if add==0:
        print("YES")
    else:
        print("NO")

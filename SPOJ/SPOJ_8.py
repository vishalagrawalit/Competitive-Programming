for _ in range(int(input())):
    n = int(input())
    add = 0
    men = list(map(int,input().split()))
    women = list(map(int,input().split()))
    men.sort()
    women.sort()
    for i in range(n):
        add += men[i]*women[i]
    print(add)

M = 10**6 + 7
for _ in range(int(input())):
    n = int(input())
    stand = (n * (1+n))//2
    stand = stand % M
    print(((2*stand) - (n*(n-1))//2)%M)

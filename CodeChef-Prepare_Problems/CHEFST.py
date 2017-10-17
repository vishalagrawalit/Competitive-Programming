for _ in range(int(input())):
    n, m, k = map(int, input().split())
    k = (k*(k+1))//2
    print(m+n-2*(min(n, m , k)))

for _ in range(int(input())):
    n = int(input())
    maxi, y = 4294967295, 10**5
    
    x = ((maxi+1 - 2*y)//(n-1)) + 1

    if (2*y + (n-1)*x):
        y = ((maxi+1) - (n-1)*x + 1)//2

    #print(x, y)

    ans = str(y) + " "
    for i in range(1, n):
        ans += str(x) + " "
        
    print(ans)

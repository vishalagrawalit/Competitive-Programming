n = float(input())
while n!=0.00:
    i,ans=2,0
    while ans<=n:
        ans+=1/i
        i+=1
    print(str(i-2) + " card(s)")
    n = float(input())

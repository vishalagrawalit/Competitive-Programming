for _ in range(int(input())):
    a,b = map(int,input().split())
    p,q = a%10, b%4
    if b==0:
        print(1)
    elif p==0 or p==1 or p==5 or p==6:
        print(p)
    elif q==1:
        print(p)
    elif q==2:
        print((p*p)%10)
    elif q==3:
        print((p**3)%10)
    elif q==0:
        print((p**4)%10)

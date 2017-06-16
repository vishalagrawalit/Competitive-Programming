n = int(input())
if n==1 | n==0 | n==2:
    print(n)
if n%2!=0:
    print(0)
else:
    add = 0
    while n%2==0:
        n = n//2
        add+=2
    print(add)

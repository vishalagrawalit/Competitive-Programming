from math import sqrt
n = int(input())
if n==1:
    print(1)
elif n>1 and n<9:
    print(n + (n//2) -1)
else:
    add = 0
    for i in range(1,int(sqrt(n))+1):
        add += ((n//i)-(i-1))
    print(add)
        

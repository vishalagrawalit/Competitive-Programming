import math
from decimal import *
 
context = Context(prec=1000)
setcontext(context)
 
add = 0
for i in range(0,1000):
    add += Decimal(1) / Decimal(math.factorial(i))
 
 
def calculate(alpha, n):
    n_,flag = n,0
    global add
    add = 0
    while n_>0:
        if int(alpha)>=2.0:
            alpha = Decimal(alpha) - Decimal(1)
            if flag==0:
                add+=(n*(n+1))//2
            else:
                add-=(n*(n+1))//2
        else:
            n_ = math.floor((Decimal(alpha)-Decimal(1)) * Decimal(n))
            alpha = Decimal(alpha) / Decimal(alpha-1)
            if flag==0:
                add+=((n+n_) *(n+n_+1))//2
                flag = 1
            else:
                add-=((n+n_) *(n+n_+1))//2
                flag = 0
            n = n_
    return add
    
n = int(input())
 
print(calculate(add, n))

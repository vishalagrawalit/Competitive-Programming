from decimal import *

context = Context(prec=10000)
setcontext(context)

a, b, c = map(int, input().split())
string = str(Decimal(a)/Decimal(b))

flag, ans = 0, 0
for i in range(len(string)):
    if string[i]==".":
        flag = 1
    elif flag==1:
        ans+=1
        if string[i]==str(c) and i<9999:
            print(ans)
            flag=-1
            break
if Decimal(float(string))*Decimal(b) == a and c==0:
    print(ans+1)
elif flag==1:
    print(-1)

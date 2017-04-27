#Add two numbers without using +,++,--,-

def add(x,y):
    while (y!=0):
        carry = x & y
        x ^= y
        y = carry << 1
    return x

for _ in range(int(input())):
    a = int(input())
    b = int(input())
    print(add(a,b))

from math import sqrt

def output(n):
    add = 0
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            if n//i==i:
                add+=i
            else:
                add+=i+n//i
    return add

for _ in range(int(input())):
    n = int(input())
    print(output(n) - n)

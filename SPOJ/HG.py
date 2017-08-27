import math
from collections import Counter

def primeFactors(n, arr):
    while n % 2 == 0:
        arr.append(2)
        n = n // 2

    for i in range(3,int(math.sqrt(n))+1,2):

        while n % i== 0:
            arr.append(i)
            n = n // i
            
    if n > 2:
        arr.append(n)

    return arr

        
n = int(input())
arra = list(map(int, input().split()))

m = int(input())
arrb = list(map(int, input().split()))

factor_a = []
for i in range(n):
    factor_a = primeFactors(arra[i], factor_a)

factor_b = []
for i in range(m):
    factor_b = primeFactors(arrb[i], factor_b)

set_a = Counter(factor_a)
set_b = Counter(factor_b)

sets = list(set(factor_a))

ans = 1
for i in range(len(sets)):
    if set_a[sets[i]]!=0 and set_b[sets[i]]!=0:
        ans *= sets[i]**(min(set_a[sets[i]], set_b[sets[i]]))
        
print((str(ans))[-9:])
        

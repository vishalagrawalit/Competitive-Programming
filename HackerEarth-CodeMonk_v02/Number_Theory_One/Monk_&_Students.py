from bisect import bisect_right, insort_left
 
def gcd(a, b):
    if min(a,b) == 0:
        return max(a, b)
    return gcd(b, a%b)
 
n = int(input())
arr  = []
for i in range(n):
    a, b, c, d = map(int, input().split())
    gcds = gcd(abs(c - a), abs(d - b)) + 1
    insort_left(arr, (gcds, i + 1))
 
for _ in range(int(input())):
    x = int(input())
    index = bisect_right(arr, (x, -1))
    if index == n:
        print(-1)
    else:
        print(arr[index][1])

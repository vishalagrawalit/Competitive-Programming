n = int(input())
arr = list(map(int,input().split()))

arr.sort()
last = 0

for i in range(n):
    last += (arr[n-i-1] * (2**i))

print(last)

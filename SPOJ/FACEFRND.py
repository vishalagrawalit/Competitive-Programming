lis = []
n = int(input())
for _ in range(n):
    arr = list(map(int,input().split()))
    lis += list(arr[2:])
print(len(set(lis)) - n)

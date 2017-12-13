from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

count = Counter(arr)
sets = list(set(arr))

maxi = -1
for i in range(len(sets)):
    maxi = max(count[sets[i]], maxi)

print(maxi)


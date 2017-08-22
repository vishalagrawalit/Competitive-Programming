from statistics import median
from heapq import heappush

queue = []
for _ in range(int(input())):
    n = int(input())
    heappush(queue, n)

    print(int(median(queue)))

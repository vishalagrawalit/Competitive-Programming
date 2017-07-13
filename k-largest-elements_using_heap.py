import heapq

for _ in range(int(input())):
    n, k = map(int,input().split())
    
    arr = list(map(int,input().split()))

    heapq.heapify(arr)

    answer = heapq.nlargest(k, arr)
    print(*answer, sep=" ")

n = int(input())
arr = list(map(int,input().split()))
q, x = map(int,input().split())

bag, flag = [], 0

for _ in range(q):
    s = input()
    if s=="Harry":
        bag.insert(0, arr.pop(0))
    else:
        bag.pop(0)
    if sum(bag)==x and flag==0:
        flag = 1
        print(len(bag))
if flag==0:
    print(-1)

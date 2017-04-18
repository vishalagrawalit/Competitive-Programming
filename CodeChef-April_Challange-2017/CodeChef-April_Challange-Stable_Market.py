import itertools

for _ in range(int(input())):
    s = input().split()
    n,q = int(s[0]),int(s[1])
    arr = list(map(int,input().split()))
    for _ in range(q):
        count=0
        query = list(map(int,input().split()))
        newlist = arr[query[0]-1 : query[1]]
        cons = [(len(list(x[1]))) for x in itertools.groupby(newlist)]
        for i in range(len(cons)):
            if cons[i]>=query[2]:
                count+=1
        print(count)

            

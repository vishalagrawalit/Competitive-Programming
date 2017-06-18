def schedule(n, ):
    lis = [None]*n
    j = 0
    for i in new.items():
        lis[j] = i[1][1]
        j+=1

    for i in range(1,n):
        for j in range(i):
            if 
    

dic = {}
n = int(input())
for _ in range(n):
    query = input().split()
    start,last,value = int(query[0]),int(query[1]),int(query[2])
    dic.update({start:[last,value]})
new = sorted(dic.items(), key=lambda x: x[1][0])


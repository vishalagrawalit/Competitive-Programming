test = int(input())
lis = [0]*(test+1)
lis[0]=0
last = 1000000
for i in range(1,test+1):
    n = int(input())
    if n>last:
        lis[i]=lis[i-1]+1
    else:
        lis[i]=1
    last = n

print(sum(lis))

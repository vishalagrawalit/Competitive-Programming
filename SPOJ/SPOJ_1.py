num=int(input())
a=[]
while num!=42:
    a.append(num)
    num = int(input())
for i in range(len(a)):
    print (a[i])

from math import sqrt

s = input().split()
a,b = int(s[0]),int(s[1])
ans = 0

while a!=1:
    count,arr = 0,[]
    for i in range(1,int(sqrt(a))+1):
        if a%i==0:
            count+=1
            if a//i==i:
                arr.append(i)
            else:
                if i==1:
                    arr.append(i)
                else:
                    arr.append(i)
                    arr.append(a//i)
    a = max(arr)
    ans += len(arr)+1
    print(ans)

while b!=1:
    count,arr = 0,[]
    for i in range(1,int(sqrt(b))+1):
        if b%i==0:
            count+=1
            if b//i==i:
                arr.append(i)
            else:
                if i==1:
                    arr.append(i)
                else:
                    arr.append(i)
                    arr.append(b//i)
    b = max(arr)
    ans+=len(arr)+1
    print("B",ans)
    
print(ans)


            

n=int(input())
arra = list(map(int,input().split()))
arrb = list(map(int,input().split()))

#sort the lists
arra.sort()
arrb.sort()

#traverse a 
j,count=0,0
for i in range(n):
    if j==n:
        break
    while j<n:
        if arra[i]==arrb[j]:
            count+=1
            j+=1
            break
        elif arra[i]<arrb[j]:
            break
        else:
            j+=1

if count==n:
    print(count-1)
else:
    print(count+1)

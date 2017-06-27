s = input()
even = ["2", "4", "6", "8", "0"]

lis = [0]*len(s)

count=0
    
for i in range(len(s)-1,-1,-1):
    if s[i] in even:
        count+=1
        lis[i]=count
    else:
        lis[i] = count

print(*lis,sep=" ")

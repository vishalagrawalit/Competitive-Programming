s = input().split()
lis= []

for i in range(len(s[0])):
    lis.append(s[0][i:])
    
#print(lis)
lis.sort()
print(lis[int(s[1])-1])

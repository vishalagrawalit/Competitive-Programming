test=int(input())

a = []
dp=[0]*(test)
for i in range(0,test):
    a.append(int(input()))
dp[0]=1
    
for i in range(1,test):
    if a[i]>a[i-1]:
        dp[i]+=dp[i-1]+1
    else:
        dp[i]=1

for j in range(test-2,-1,-1):
    if a[j]>a[j+1] and dp[j]<=dp[j+1]:
        dp[j]=dp[j+1]+1
        
print(sum(dp))

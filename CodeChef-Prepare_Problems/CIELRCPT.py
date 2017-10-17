arr = [1,2,4,8,16,32,64,128,256,512,1024,2048]
for _ in range(int(input())):
    n = int(input())
    count = 0
    for i in range(11,-1,-1):
        if n//arr[i]>0:
            count+=(n//arr[i])
            n -= (n//arr[i] * arr[i])
        if n==0:
            break
    print(count)
            
        

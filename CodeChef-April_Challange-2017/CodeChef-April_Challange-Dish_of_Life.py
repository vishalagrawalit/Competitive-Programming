for _ in range(int(input())):
    s = input().split()
    n,k = int(s[0]),int(s[1])
    lis = [0]*k
 
    breakpoint,newList,breaker,count=0,[],0,0
    for x in range(n):
        query = list(map(int,input().split()))
        if query[0]==k:
            breaker = 1
            break
        
        for i in range(1,int(query[0])+1):
            if lis[query[i]-1]==0:
                lis[query[i]-1]=1
                count+=1
                if count==k and x==n-1:
                    breakpoint = 0
                    break
                elif count==k:
                    breakpoint=1
                    break
                
    if breakpoint==1:
        print("some")
    elif breaker==1:
        print("some")
    elif count!=k:
        print("sad")
    else:
        print("all")

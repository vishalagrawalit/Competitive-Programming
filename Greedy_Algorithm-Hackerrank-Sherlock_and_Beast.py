for _ in range(int(input())):
    n = int(input())
    ans=[]
    for i in range(0,n+1,5):
        if (n-i) % 3==0:
            ans = ["5"]*(n-i) + ["3"]*i
            break
    if ans==[]:
        print(-1)
    else:
        print(*ans,sep="")

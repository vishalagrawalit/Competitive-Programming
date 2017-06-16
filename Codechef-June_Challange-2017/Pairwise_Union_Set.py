for _ in range(int(input())):
    v = [[0]*2501 for i in range(2501)]
    a = [0]*5005
    n,k = map(int,input().split())
    pp , cc =0,0

    for i in range(n):
        x = list(map(int,input().split()))
        if x[0]==k:
            cc+=1
        else:
            a[pp]=x[0]
            for j in range(1,a[pp]+1):
                v[pp][x[j]]=1
            pp+=1

    if pp!=0 and cc!=0:
        ans = cc * pp + (cc * (cc-1))//2
    else:
        ans = (cc * (cc - 1))//2

    for i in range(pp):
        for j in range(i+1,pp):
            if a[i]+a[j]>=k:
                ass = 0
                for f in range(1,k+1):
                    if v[i][f]!=1 and v[j][f]!=1:
                        break
                    else:
                        ass+=1
                if ass==k:
                    ans+=1

    print(ans)

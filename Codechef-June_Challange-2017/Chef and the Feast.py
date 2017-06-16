for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    answer,count,add = 0,0,0
    arr.sort()
    for i in range(n-1,-1,-1):
        if arr[i]>=0:
            add+=arr[i]
            count+=1
        else:
            if count*add <= (count+1)*(add+arr[i]):
                count+=1
                add+=arr[i]
            else:
                answer += arr[i]
    answer += count*add
    print(answer)

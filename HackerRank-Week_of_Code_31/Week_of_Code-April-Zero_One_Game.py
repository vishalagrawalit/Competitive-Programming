for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    one,zero=0,0
    for i in range(1,n-1):
        if arr[i]==1 and arr[i-1]==0 and arr[i+1]==0:
            one+=1
            arr[i]=3
    for j in range(1,n-1):
        if arr[j]==0 and (arr[j-1]==0 or arr[j-1]==3) and (arr[j+1]==3 or arr[j+1]==0):
            zero+=1
            
    if (one+zero)%2==1:
        print("Alice")
    else:
        print("Bob")

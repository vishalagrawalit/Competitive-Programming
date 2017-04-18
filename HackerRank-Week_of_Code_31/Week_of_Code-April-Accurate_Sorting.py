for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    new = sorted(arr)
    if new==arr:
        print("Yes")
    else:
        i=0
        while i!=n-1:
            if arr[i]!=i:
                if arr[i]==i+1 and arr[i+1]==i:
                    arr[i],arr[i+1]=arr[i+1],arr[i]
                else:
                    print("No")
                    break
            i+=1
            if i==n-1:
                print("Yes")
             

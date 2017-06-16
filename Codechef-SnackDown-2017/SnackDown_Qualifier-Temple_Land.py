for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    if n%2==0:
        print("no")
    else:
        if arr[0]==1 and arr[n-1]==1:
            for i in range(n-1):
                if i<n//2:
                    if arr[i+1]-arr[i]!=1:
                        print("no")
                        break
                elif i>=n//2:
                    if arr[i]-arr[i+1]!=1:
                        print("no")
                        break
            else:
                print("yes")
        else:
            print("no")

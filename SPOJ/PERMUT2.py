n = int(input())
while n!=0:
    arr = list(map(int,input().split()))
    for i in range(n):
        if arr[arr[i]-1]!=i+1:
            print("not ambiguous")
            break
    else:
        print("ambiguous")
    n = int(input())

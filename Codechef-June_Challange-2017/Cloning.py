for _ in range(int(input())):
    n,q = map(int,input().split())
    arr = list(map(int,input().split()))
    for i in range(q):
        a,b,c,d = map(int,input().split())
        
        arr1 = arr[a-1:b]
        arr1.sort()
        arr2 = arr[c-1:d]
        arr2.sort()
        check = 0
        
        for j in range(b-a+1):
            if arr1[j]!=arr2[j]:
                check+=1
            if check == 2:
                check = -1
                print("NO")
                break
        if check!=-1:
            print("YES")
                

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    
    i,j = 0,n-1
    mini = 10**6
    
    arr.sort()
    
    while i<j:
        add = arr[i] + arr[j]
        
        if mini > abs(add):
            mini = abs(add)
            left, right = arr[i], arr[j]

        if add<0:
            i+=1
        elif add>0:
            j-=1
        else:
            left, right = arr[i], arr[j]
            break
        
    print(left, right)

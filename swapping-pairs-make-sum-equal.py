for _ in range(int(input())):
    m, n = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))

    diff = (sum(arr1)-sum(arr2))

    if diff%2!=0:
        print(-1)

    else:
        i,j = 0, 0
        diff = diff//2
        while i<m and j<n:
            if arr1[i]-arr2[j] == diff:
                print(1)
                break
            elif arr1[i]-arr2[j] > diff:
                j+=1
            else:
                i+=1
        else:
            print(-1)

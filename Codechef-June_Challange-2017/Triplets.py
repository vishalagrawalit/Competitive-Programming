def binarySearch(arr, l, r, x):
    if l>r:
        return -1
    if x>=arr[r]:
        return r
 
    mid = (l+r)//2
    if arr[mid]==x:
        return mid
 
    if mid>0 and arr[mid-1]<= x and x<arr[mid]:
        return mid-1
 
    if x<arr[mid]:
        return binarySearch(arr, l, mid-1, x)
 
    return binarySearch(arr, mid+1, r, x)
 
 
 
M = 10**9 + 7
for _ in range(int(input())):
    array = list(map(int,input().split()))
    s_one,s_three = [],[]
    p = list(map(int,input().split()))
    p.sort()
    
    add = 0
    for x in range(array[0]):
        add = (add+p[x])%M
        s_one.append(add)
               
    q = list(map(int,input().split()))
    q.sort()
 
    r = list(map(int,input().split()))
    r.sort()
    
    add = 0
    for x in range(array[2]):
        add = (add+r[x])%M
        s_three.append(add)
 
    ans = 0
 
    for i in range(array[1]):
        index_p = binarySearch(p,0, array[0]-1, q[i])
        index_r = binarySearch(r,0, array[2]-1, q[i])

        if index_p < array[0] and index_p!=-1 and p[index_p+1]==q[i]:
            for j in range(index_p+1,array[0]-1):
                if p[j]==q[i]:
                    index_p+=1
                else:
                    break

        if index_r < array[2] and index_r!=-1 and r[index_r+1]==q[i]:
            for k in range(index_r+1,array[2]-1):
                if r[k]==q[i]:
                    index_r+=1
                else:
                    break
 
        if index_p!=-1 and index_r!=-1:
            res = (q[i] * q[i] * (index_p+1) * (index_r+1)) + (s_one[index_p] * s_three[index_r]) + (s_one[index_p] * (index_r+1) + s_three[index_r] * (index_p+1)) * q[i]
            ans = (ans + (res%M))%M
 
    print(ans)

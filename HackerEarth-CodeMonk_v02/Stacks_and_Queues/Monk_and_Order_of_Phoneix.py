def ceilsearch(arr, n, x):
    low, high = 0, n-1
    ceil = -1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==x:
            return arr[mid]
        elif x<arr[mid]:
            ceil = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
    return ceil
            

n = int(input())
matrix = []

for _ in range(n):
    arr = list(map(int,input().split()))
    matrix.append(arr[1:])

q = int(input())
for _ in range(q):
    s = input().split()
    if s[0]=="0":
        index = int(s[1])
        matrix[index-1].pop(-1)
    elif s[0]=="1":
        x, y = int(s[1]), int(s[2])
        if x==1:
            matrix[x-1].append(y)
        else:
            matrix[x-1].append(y)
            matrix[x-1].sort()
    else:
        mini = min(matrix[0])
        flag = 0
        for i in range(1,n):
            #print(mini)
            index = ceilsearch(matrix[i], len(matrix[i]), mini+1)
            if index!=-1:
                mini = index
                flag = 1
            else:
                flag = 0
                break
        if flag==1:
            print("YES")
        else:
            print("NO")

n = int(input())

a = list(map(int, input().split()))
matrix = []

count = 1
for i in range(n-1):
    if a[i+1]>a[i] and i!=n-2:
        count+=1
    elif a[i+1]<a[i] and i!=n-2:
        matrix.append((count, i))
        count = 1
    elif i==n-2 and a[i+1]>a[i]:
        count+=1
        matrix.append((count, i+1))
    elif i==n-2 and a[i+1]<a[i]:
        matrix.append((count, i))
        matrix.append((1, i+1))

print(matrix)
ans, res = -1, 10**5+2

for i in range(len(matrix)-1):
    if matrix[i][1]>0 and matrix[i][1]<n-2:
        if a[matrix[i][1] -1] < a[matrix[i][1]+1]:
            if ans < matrix[i][0]+matrix[i+1][0]-1:
                ans = matrix[i][0]+matrix[i+1][0]-1
                res = a[matrix[i][1]]
            elif ans == matrix[i][0]+matrix[i+1][0]-1:
                res = min(res, a[matrix[i][1]])
        if a[matrix[i][1]]<a[matrix[i][1]+2]:
            if ans < matrix[i][0]+matrix[i+1][0]-1:
                ans = matrix[i][0]+matrix[i+1][0]-1
                res = a[matrix[i][1]+1]
            elif ans == matrix[i][0]+matrix[i+1][0]-1:
                res = min(res, a[matrix[i][1]+1])
    elif matrix[i][1]==0:
        res = a[matrix[i][1]]
        ans = a[matrix[i+1][1]]

if len(matrix)==1 or n==1:
    print(min(a))
else:
    print(res)






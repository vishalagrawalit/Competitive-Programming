n, x, y = map(int, input().split())

andy = list(map(int, input().split()))
bob = list(map(int, input().split()))

matrix = []
for i in range(n):
    matrix.append(( andy[i], bob[i], abs(andy[i]-bob[i]) ))

matrix.sort(key=lambda x:x[2])

add = 0
for i in range(n-1, -1, -1):
    if matrix[i][0]>matrix[i][1]:
        if x>0:
            add+=matrix[i][0]
            x-=1
        else:
            add+=matrix[i][1]
            y-=1
    elif matrix[i][0]<=matrix[i][1]:
        if y>0:
            add+=matrix[i][1]
            y-=1
        else:
            add+=matrix[i][0]
            x-=1
print(add)

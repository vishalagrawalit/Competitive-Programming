def total_count(matrix, x, y, count):
    for i in range(x,n):
        for j in range(y,n):
            if matrix[x][y]>matrix[i][j]:
                count+=1
    return count

for _ in range(int(input())):
    n = int(input())
    matrix = []
    for i in range(n):
        arr = list(map(int,input().split()))
        matrix.append(arr)
    add = 0
    for i in range(n):
        for j in range(n):
            add += total_count(matrix, i , j, 0)

    print(add)

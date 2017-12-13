n = int(input())
arr = list(map(int, input().split()))

add = 0
matrix = {}
lookup = []

value = 0
for i in range(n-1, -1, -1):
    if arr[i] in lookup:
        x = matrix[arr[i]][0]
        add+=matrix[arr[i]][1]
    else:
        lookup.append(arr[i])
        x = n
    for j in range(i+1, x):
        if -1 <= arr[i]-arr[j] <= 1:
            add+=0
            value = 0
        else:
            add+=(-1 * (arr[i]-arr[j]))
            value = (-1 * (arr[i]-arr[j]))
    matrix.update({arr[i]:(i, value)})
print(add)

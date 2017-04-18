from itertools import combinations

query = input().split()
n,m = int(query[0]),int(query[1])

arr = list(map(int,input().split()))

lis=[0]*(max(arr)+1)

for i in range(n):
    lis[arr[i]] = 3.14159265359 * arr[i] * arr[i]

tot_area = sum(lis)
    
list_of_combinations = list(combinations(arr,m+1))
print(list_of_combinations)
ans = 0

for i in range(len(list_of_combinations)):
    left_area = tot_area
    add = 0
    for j in range(m+1):
        add += list_of_combinations[i][j]
        left_area -= lis[list_of_combinations[i][j]]
    ans += (3.14159265359 * add * add) + left_area

print("{0:.10f}".format(ans/len(list_of_combinations)))

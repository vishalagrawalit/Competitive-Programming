import bisect

arr1 = [2,3,5,9,10,78]
arr2 = [4,6,8,11,35,95]

for i in range(len(arr2)):
    bisect.insort(arr1, arr2[i])
    
print(*arr1, sep=" ")

lis = []
for i in range(int(input())):
    arr = input()
    lis.append(arr)
    lis.sort()
    print(lis.index(arr))

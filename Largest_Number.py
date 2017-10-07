arr = [3, 30, 34, 5, 9]

def compare(x, y):
    first = str(x) + str(y)
    second = str(y) + str(x)
        
    if(first>second):
        return 1
    else:
        return 0

arr.sort(key=lambda x: compare)

print(arr)

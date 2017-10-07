def search(arr,l,r,key):
    while(r-l>1):
        m = l+(r-l)//2
        if (arr[m] >= key):
            r = m
        else:
            l = m
    return r

def sequence(arr):
    if len(arr)==0:
        return 0
    tail = [0]*len(arr)
    length = 1
    tail[0] = arr[0]

    for i in range(1,len(arr)):
        if arr[i] < tail[0]:
            tail[0] = arr[i]
        elif arr[i] > tail[length - 1]:
            tail[length]=arr[i]
            length +=1
        else:
            tail[search(tail, -1, length-1, arr[i])] = arr[i]

    return length

arr = [2,5,3,7,11,8,10,13,6,75]
print(sequence(arr))

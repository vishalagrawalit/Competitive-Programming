arr = ['1', '11', '21', '1211', '111221']
def countAndSay(A):
    if 1<=A<=len(arr):
        return arr[A-1]
    else:
        for i in range(5, A):
            string = ''
            count = 0
            for j in range(len(arr[i-1])-1):
                if arr[i-1][j]==arr[i-1][j+1]:
                    count+=1
                    if j==len(arr[i-1])-2:
                        string += str(count+1) + arr[i-1][j]
                else:
                    string += str(count+1) + arr[i-1][j]
                    count = 0
                    if j==len(arr[i-1])-2:
                        flag=1
                        string += '1' + arr[i-1][len(arr[i-1])-1]
                     
            arr.append(string)
    return arr[A-1]

print(countAndSay(7))

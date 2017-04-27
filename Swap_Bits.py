for _ in range(int(input())):
    arr = list(map(int,input().split()))
    b = bin(arr[0])[2:]

    binary = list(b)
    
    i = 0
    while i<arr[3]:
        if len(binary)-arr[1]-1-i >= 0 and len(binary)-arr[2]-1-i >= 0:
           binary[len(binary)-arr[1]-1-i],binary[len(binary)-arr[2]-1-i] = binary[len(binary)-arr[2]-1-i],binary[len(binary)-arr[1]-1-i]
        elif len(binary)-arr[2]-1-i < 0:
            binary.insert(0,'0')
            binary[len(binary)-arr[1]-1-i],binary[len(binary)-arr[2]-1-i] = binary[len(binary)-arr[2]-1-i] , binary[len(binary)-arr[1]-1-i]
        i+=1

    binary = ''.join(binary)
   
    print(int(binary , 2))

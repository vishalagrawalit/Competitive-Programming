for _ in range(int(input())):
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))

    if arr1[1] == arr1[3]:
        
        if arr2[1] == arr2[3] and (min(arr2[0],arr2[2]) <= max(arr1[0],arr1[2])) and (max(arr2[0],arr2[2]) >= min(arr1[0],arr1[2])):
            print("yes")
            
        elif arr2[0]==arr1[0] and arr2[1]==arr1[1]:
            print("yes")

        elif arr2[0]==arr1[2] and arr2[1]==arr1[3]:
            print("yes")

        elif arr2[2]==arr1[0] and arr2[3]==arr1[1]:
            print("yes")

        elif arr2[2]==arr1[2] and arr2[3]==arr1[3]:
            print("yes")
            
        else:
            print("no")
    
    elif arr1[0] == arr1[2]:
        
        if arr2[0] == arr2[2] and (min(arr2[1],arr2[3]) <= max(arr1[1],arr1[3])) and (max(arr2[1],arr2[3]) >= min(arr1[1],arr1[3])):
            print("yes")
            
        elif arr2[0]==arr1[0] and arr2[1]==arr1[1]:
            print("yes")

        elif arr2[0]==arr1[2] and arr2[1]==arr1[3]:
            print("yes")

        elif arr2[2]==arr1[0] and arr2[3]==arr1[1]:
            print("yes")

        elif arr2[2]==arr1[2] and arr2[3]==arr1[3]:
            print("yes")
            
        else:
            print("no")

    else:
        print("no")


for _ in range(int(input())):
    k = int(input())
    s = input()
    arr = list(s)
    n = len(arr)
    if arr[0]==arr[n-1] and arr[0]!="?":
        print("NO")
    else:
        for i in range(n):
            if i!=n-1 and arr[i]=="?":
                if arr[i-1]!="0" and arr[i+1]!="0":
                    arr[i] = "0"
                elif arr[i-1]!="1" and arr[i+1]!="1" and k>=2:
                    arr[i]= "1"
                elif arr[i-1]!="2" and arr[i+1]!="2" and k>=3:
                    arr[i]= "2"
                else:
                    print("NO")
                    break
            elif i==n-1 and arr[i]=="?":
                if arr[i-1]!="0" and arr[0]!="0":
                    arr[i]= "0"
                elif arr[i-1]!="1" and arr[0]!="1" and k>=2:
                    arr[i]= "1"
                elif arr[i-1]!="2" and arr[0]!="2" and k>=3:
                    arr[i]= "2"
                else:
                    print("NO")
                    break
            elif arr[i]!="?":
                if i!=n-1 and (arr[i-1]==arr[i] or arr[i]==arr[i+1]):
                    print("NO")
                    break
                if i==n-1 and (arr[i-1]==arr[i] or arr[i]==arr[0]):
                    print("NO")
                    break
        else:
            print(*arr,sep="")
            
                

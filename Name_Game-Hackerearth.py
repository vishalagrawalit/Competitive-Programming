a = [ 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113 ]
t=int(input())
for j in range(t):
    n = int(input())
    s = input()
    i=0
    while(i<n):
        ch=ord(s[i])
        flag=1
        for k in range(12):
            if(ch==a[k]):
                flag=0
                break
        if(flag==0):
            print(s[i], end="")
        else:
            if(ch>=113):
                print(chr(113), end="")
            elif(ch<=67):
                print(chr(67), end="")
            else:
                for k in range(11):
                    if(ch>a[k] and ch<a[k+1]):
                        if (ch-a[k])<=(a[k+1]-ch):
                            ch =  a[k]
                        else:
                            ch = a[k+1]
                print(chr(ch), end="")
        i+=1
    print()

for _ in range(int(input())):
    string = input()+" "
    ans,zero,one=0,0,0
    for i in range(len(string)):
        if (string[i]=="1" or string[i]==" ") and zero>=1:
            ans+=(one * (zero+1))
            zero=0
            one+=1
        elif string[i]=="1":
            one+=1
        elif string[i]=="0":
            zero+=1
    print(ans)

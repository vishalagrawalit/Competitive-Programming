for _ in range(int(input())):
    print("")
    s = input().split()

    cal = int(s[0])
    i = 1
    while i<len(s):
        if s[i]=="+":
            b = int(s[i+1])
            cal = cal + b
            i+=1
        elif s[i]=="*":
            b = int(s[i+1])
            cal = cal * b
            i+=1
        elif s[i]=="/":
            b = int(s[i+1])
            cal = int(cal/b)
            i+=1
        elif s[i]=="-":
            b = int(s[i+1])
            cal-=b
            i+=1
        elif s[i]=="=":
            break

        i+=1
    print(cal)
        
        

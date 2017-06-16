for _ in range(int(input())):
    n = int(input())
    string = input()
    check,ans = 1,0
    for i in range(n):
        if string[i]=="H" and check==1:
            check = 0
            ans+=1
        elif string[i]=="T" and check==0:
            check = 1
            ans+=1
        elif string[i]==".":
            continue
        else:
            ans=1
            break
    if ans%2==0:
        print("Valid")
    else:
        print("Invalid")
        

def checkchef(s):
    alpha = ['C','H','E','F']
    flag = 0
    for i in range(4):
        if s[i]==alpha[i] or s[i]=="?":
            continue
        else:
            flag = 1
    if flag==1:
        return False
    else:
        return True

for _ in range(int(input())):
    s = input()
    if len(s)<=3:
        ans = ""
        for i in range(len(s)):
            if s[i]=="?":
                ans+="A"
            else:
                ans+=s[i]
        print(ans)
    else:
        ans = [""]*len(s)
        i = len(s)-1
        
        while i>-1:
            if i>=3 and checkchef(s[i-3:i+1]):
                ans[i]="F"
                ans[i-1]="E"
                ans[i-2]="H"
                ans[i-3]="C"
                i-=4
            else:
                if s[i]=="?":
                    ans[i] = "A"
                else:
                    ans[i]= s[i]
                i-=1
        print(*ans,sep="")

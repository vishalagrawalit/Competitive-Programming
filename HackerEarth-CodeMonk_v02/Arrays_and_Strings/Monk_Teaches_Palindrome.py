for _ in range(int(input())):
    s = input()
    count = 0
    for i in range(len(s)//2):
        
        if s[i] == s[len(s)-1-i]:
            count+=1

    if count == len(s)//2 and len(s) % 2 ==0:
        print ("YES EVEN")

    if count == len(s)//2 and len(s) % 2 !=0:
        print ("YES ODD")

    if count != len(s)//2:
        print("NO")

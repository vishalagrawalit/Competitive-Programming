for _ in range(int(input())):
    print("")
    s = input().split()
    n1, n2 = None, None
    if int(s[0]) is int:
        n1 = int(s[0])
    if int(s[2]) is int:
        n2 = int(s[2])
    if int(s[4]) is int:
        ans = int(s[4])

    if n1!=None and n2!=None:
        print(s[0] + " + " + s[2] + " = " + str(n1+n2))

    else:
        if n1==None:
            print (str(ans-n2) + " + " + s[2] + " = " + s[4])
        else:
            print (s[0] + " + " + str(ans-n1) + " = " + s[4])

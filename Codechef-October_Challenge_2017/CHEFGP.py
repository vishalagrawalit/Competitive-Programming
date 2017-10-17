for _ in range(int(input())):
    s = input()
    x, y = map(int, input().split())
    s = list(s)
    s.sort()

    a_count, b_count = s.count("a"), s.count("b")

    ans = ""
    i = 0
    if a_count >= b_count:
        while a_count>0 and b_count>0:
            if i%2==0:
                ans += "a"
                a_count -= 1
            else:
                ans += "b"
                b_count -= 1
            i+=1
    else:
        while a_count>0 and b_count>0:
            if i%2==1:
                ans += "a"
                a_count -= 1
            else:
                ans += "b"
                b_count -= 1
            i+=1
    

    #print(ans)

    res = ""
    if len(ans)==0:
        if a_count == 0:
            j, i = 0, 0
            while i<len(s):
                if j==y:
                    res += "*"
                    j = 0
                else:
                    res+="b"
                    j+=1
                    i+=1

        elif b_count == 0:
            j, i = 0, 0
            while i<len(s):
                if j==x:
                    res += "*"
                    j = 0
                else:
                    res+="a"
                    j+=1
                    i+=1
        print(res)
    else:
        if a_count == 0:
            if y==1:
                res = ans
                j, i = 0, 0
                while i<b_count:
                    if j==y:
                        res += "*"
                        j = 0
                    else:
                        res+="b"
                        j+=1
                        i+=1
                print(res)
            else:
                for m in range(len(ans)):
                    if ans[m]=="b" and b_count>0:
                        if b_count >= y-1:
                            res += ("b")*y
                            b_count -= (y-1)
                        else:
                            res += ("b")*(b_count+1)
                            b_count -= (b_count)
                    else:
                        res += ans[m]
                if b_count>0:
                    j, i = 0, 0
                    while i<b_count:
                        if j==y:
                            res += "*"
                            j = 0
                        else:
                            res+="b"
                            j+=1
                            i+=1
                print(res)

        elif b_count==0:
            if x==1:
                res = ans
                j, i = 0, 0
                while i<a_count:
                    if j==x:
                        res += "*"
                        j = 0
                    else:
                        res+="a"
                        j+=1
                        i+=1
                print(res)
            else:
                for m in range(len(ans)):
                    if ans[m]=="a" and a_count>0:
                        if a_count >= x-1:
                            res += ("a")*x
                            a_count -= (x-1)
                        else:
                            res += ("a")*(a_count+1)
                            a_count -= a_count
                    else:
                        res += ans[m]
                if a_count>0:
                    j, i = 0, 0
                    while i<a_count:
                        if j==x:
                            res += "*"
                            j = 0
                        else:
                            res+="a"
                            j+=1
                            i+=1
                print(res)


                            
                

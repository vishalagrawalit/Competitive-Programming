for _ in range(int(input())):
    n = int(input())
    if n%7==0:
        print("YES")
    elif n%3==0:
        print("YES")
    else:
        while n>2:
            n-=3
            if n%7==0:
                print("YES")
                break
        else:
            print("NO")

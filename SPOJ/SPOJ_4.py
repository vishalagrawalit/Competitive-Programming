for _ in range(int(input())):
    x,y = map(int,input().split())
    if x-y == 2:
        if x%2==0:
            print(2*x - 2)
        else:
            print(2*x - 3)
    elif x-y == 0:
        if x%2==0:
            print(2*x)
        else:
            print(2*x-1)
    else:
        print("No Number")
        

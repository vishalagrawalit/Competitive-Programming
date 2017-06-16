for x in range(int(input())):
    borrow,no_of_frnds = map(int,input().split())
    new_arr = list(map(int,input().split()))
    arr = sorted(new_arr,reverse=True)
    add = 0
    for i in range(no_of_frnds):
        add+=arr[i]
        if add>=borrow:
            print("Scenario #"+str(x+1))
            print(i+1)
            print("")
            break
    else:
        print("Scenario #"+str(x+1))
        print("Impossible")
        print("")

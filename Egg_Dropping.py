def dropping(eggs, floors):
    M = 10**18
    lis = [[0]*(floors+1) for x in range(eggs+1)]

    for i in range(floors+1):
        lis[1][i] = i

    for e in range(2,eggs+1):
        for f in range(1,floors+1):
            lis[e][f] = M
            for k in range(1,f+1):
                c = 1+max(lis[e-1][k-1], lis[e][f-k])
                if c<lis[e][f]:
                    lis[e][f] = c
    return lis[eggs][floors]

number_of_eggs = int(input())
number_of_floors = int(input())

print(dropping(number_of_eggs , number_of_floors))

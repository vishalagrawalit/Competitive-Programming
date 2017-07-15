for _ in range(int(input())):
    n = int(input())

    mod = (11 + (8*(n%11)))%11

    if mod==0:
        print(0)
    else:
        print(11 - mod)

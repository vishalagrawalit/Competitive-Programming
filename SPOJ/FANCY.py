for _ in range(int(input())):
    n = input()
    count, ans = 0, 1
    for i in range(len(n)-1):
        if n[i]!=n[i+1]:
            ans *= (2**count)
            count = 0
        elif i == len(n)-2:
            ans *= (2**(count+1))
        else:
            count += 1
    print(ans)

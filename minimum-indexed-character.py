for _ in range(int(input())):
    s1 = input()
    s2 = input()

    s2 = list(set(s1))

    mini = 10**6

    for i in range(len(s2)):
        if s2[i] in s1:
            mini = min(s1.index(s2[i]), mini)
            ans = s2[i]

    print(ans)
            

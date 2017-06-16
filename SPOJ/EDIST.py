for _ in range(int(input())):
    a = input()
    b = input()
    count = 0
    for i in range(len(a)):
        if i<len(b):
            if a[i]!=b[i]:
                count+=1
        else:
            break

    print(count + abs(len(b)-len(a)))

for _ in range(int(input())):
    n = int(input())
    if n==1:
        print(1)
    elif n==2:
        print("1 " + "2")
    else:
        lis = [1,2]
        for i in range(2,n):
            x = lis[len(lis)-1]
            j = x + 1
            y = 0
            while j > x and y < len(lis):
                if j != x + lis[y] and y == len(lis)-2:
                    x = j
                    lis.append(j)
                    break
                elif j != x + lis[y]:
                    y+=1
                else:
                    j+=1
        print(*lis,sep=" ")

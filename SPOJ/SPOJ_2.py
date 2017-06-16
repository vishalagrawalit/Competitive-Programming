for i in range(int(input())):
    s = input().split()
    first,second = s[0],s[1]
    first = int(first[::-1])
    second = int(second[::-1])
    first += second
    print(int(str(first)[::-1]))
    

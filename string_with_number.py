for _ in range(int(input())):
    s = input()
    
    integer = ''
    
    for i in range(len(s), 0, -1):
        if s[i-1].isdigit():
            integer = s[i-1] + integer
        else:
            break
    if i==int(integer):
        print(1)
    else:
        print(0)
            

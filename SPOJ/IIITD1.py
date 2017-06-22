for _ in range(int(input())):
    s = int(input())
    if s>=0:
        zero = len(str(s))-1
        print("1"+"0"*zero)
    else:
        zero = len(str(s))-2
        pos = -2*s + int("1"+"0"*zero)
        print(pos)

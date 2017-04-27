def signs(a,b):
    if a^b < 0:
        return True
    else:
        return False

for _ in range(int(input())):
    s = input().split()
    a,b = int(s[0]),int(s[1])
    print(signs(a,b))

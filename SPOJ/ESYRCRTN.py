arr = [1, 3, 2, -1, -3, -2]
for _ in range(int(input())):
    n = int(input())
    modulo = n%6
    if modulo==0:
        print(0)
    elif modulo==1:
        print(1)
    elif modulo==2:
        print(4)
    elif modulo==3:
        print(6)
    elif modulo==4:
        print(5)
    elif modulo==5:
        print(2)
    
    

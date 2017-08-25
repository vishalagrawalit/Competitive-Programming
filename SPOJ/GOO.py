for _ in range(int(input())):
    number = int(input())
    value = 2**(number-1)
    print(value, (value + (value//2)*(number-1)))

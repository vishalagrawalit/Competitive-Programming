for _ in range(int(input())):
    x = int(input())

    queue = [0]

    for i in range(1,10):
        stack = []
        stack.append(i)
        num = stack.pop(0)
        while num<=x:
            queue.append(num)
            last_digit = num%10

            if last_digit==0:
                stack.append(num*10 + 1)

            elif last_digit==9:
                stack.append(num*10 + 8)

            else:
                num1 = num*10 + last_digit - 1
                num2 = num*10 + last_digit + 1

                stack.append(num1)
                stack.append(num2)

            num = stack.pop(0)

    print(*queue, sep=" ")
            
                

            

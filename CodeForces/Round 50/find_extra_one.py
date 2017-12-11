left, right = 0, 0
for i in range(int(input())):
    x, y = map(int, input().split())
    if x>0:
        right+=1
    else:
        left+=1

if left>1 and right>1:
    print("No")
else:
    print("Yes")

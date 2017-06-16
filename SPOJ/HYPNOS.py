n = input()
count=0
while True:
    count+=1
    add = 0
    for i in range(len(str(n))):
        add+=(int(n[i])*int(n[i]))
    if len(str(add))==1 and add==1:
        print(count)
        break
    elif len(str(add))==1 and add!=1:
        print(-1)
        break
    else:
        n = str(add)

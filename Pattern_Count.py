for _ in range(int(input())):
    value = input()
    flag,count=0,0
    for i in range(1,len(value)):
        if value[i]=="0" and value[i-1]=="1":
            flag=1
        elif value[i]=="1" and flag==1:
            count+=1
            flag = 0
        elif value[i]!="0" and value[i]!="1":
            flag=0
            
    print(count)

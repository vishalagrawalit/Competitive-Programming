for _ in range(int(input())):
    n = int(input())
    s = input()
    arr = [0]*8
    for i in range(38):
        if s[i]=="T" and s[i+1]=="T" and s[i+2]=="T":
            arr[0]+=1
        elif s[i]=="T" and s[i+1]=="T" and s[i+2]=="H":
            arr[1]+=1
        elif s[i]=="T" and s[i+1]=="H" and s[i+2]=="T":
            arr[2]+=1
        elif s[i]=="T" and s[i+1]=="H" and s[i+2]=="H":
            arr[3]+=1
        elif s[i]=="H" and s[i+1]=="T" and s[i+2]=="T":
            arr[4]+=1
        elif s[i]=="H" and s[i+1]=="T" and s[i+2]=="H":
            arr[5]+=1
        elif s[i]=="H" and s[i+1]=="H" and s[i+2]=="T":
            arr[6]+=1
        elif s[i]=="H" and s[i+1]=="H" and s[i+2]=="H":
            arr[7]+=1
    print(n, *arr,sep=" ")

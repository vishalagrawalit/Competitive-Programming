n = int(input())
while n!=0:
    string = input()
    words = len(string)//n
    lis = [[] for i in range(words)]
    new,ans = "",[]

    for i in range(words):
        if i%2==0:
            new += string[i*n:(i+1)*n]
            
        else:
            new += string[(i+1)*n-1:i*n-1:-1]

    for j in range(len(string)):
        lis[j%n].append(new[j])
        
    for x in range(words):
        ans += lis[x]
    print(*ans,sep="")
    n = int(input())


g, b = map(int,input().split())
while g!=-1 and b!=-1:
    if max(g,b)%(min(g,b)+1)==0:
        print(max(g,b)//(min(g,b)+1))
    else:
        print((max(g,b)//(min(g,b)+1))+1)
    g, b = map(int,input().split())

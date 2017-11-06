for _ in range(int(input())):
    a, b, c = map(int, input().split())
    d, e, f = map(int, input().split())
    g, h, i = map(int, input().split())

    k = 0
    count = 0
    
    if a>=d and b>=e and c>=f and a+b+c > d+e+f:
        count+=1
    if a<=d and b<=e and c<=f and a+b+c < d+e+f:
        count+=1
    if a>=g and b>=h and c>=i and a+b+c > g+h+i:
        count+=1
    if a<=g and b<=h and c<=i and a+b+c < g+h+i:
        count+=1
    if d>=g and e>=h and f>=i and d+e+f > g+h+i:
        count+=1
    if d<=g and e<=h and f<=i and d+e+f < g+h+i:
        count+=1

    if count==3:
        print("yes")
    else:
        print("no")

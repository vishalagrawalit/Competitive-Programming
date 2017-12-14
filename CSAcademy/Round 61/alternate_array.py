n = int(input())
arr = list(map(int, input().split()))


checka = [0,1]*n
checkb = [1,0]*n

counta, countb = 0, 0
for i in range(2*n):
    if arr[i]!=checka[i]:
        counta+=1
    if arr[i]!=checkb[i]:
        countb+=1

print((min(counta, countb))//2)

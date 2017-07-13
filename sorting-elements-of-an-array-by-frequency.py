from collections import Counter

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    
    new = Counter(arr)

    ans = []
    
    for key, value in new.items():
        ans.append([key,value])

    ans = sorted(ans,key=lambda l:l[1], reverse=True)

    new_arr = []
    for i in range(len(ans)):
        new_arr += [ans[i][0]]*ans[i][1]

    print(*new_arr,sep=" ")

from Queue import PriorityQueue

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ocup = 0
    resp = 0
    next = {}

    pos = [[] for _ in range(401)]
    for i, p in enumerate(arr):
        pos[p].append(i)
 
    cola = PriorityQueue()
    sent = [False] * 401
    for p in line:
        if not sent[p]:
            if ocup < n:
                ocup += 1
            else:
                while not cola.empty():
                    nxt, i = cola.get()
                    if pos[i][0] == -nxt:
                        sent[i] = False
                        break
            resp += 1
 
        if len(pos[p]) > 1:
            pos[p] = pos[p][1:]
            cola.put((-pos[p][0], p))
            sent[p] = True
        else:
            ocup -= 1
 
    print(resp) 


                

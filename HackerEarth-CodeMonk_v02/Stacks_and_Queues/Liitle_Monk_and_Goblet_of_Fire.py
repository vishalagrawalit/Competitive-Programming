arr = [[] for i in range(4)]
queue = []

for i in range(int(input())):
    s = input().split()
    if s[0] == "D":
        d = arr[queue[0]]
        print(d.pop(0))
        if not d:
            queue.pop(0)
    else:
        j = int(s[1])-1
        arr[j].append(s[1] + " " +s[2])
        if j not in queue:
            queue.append(j)
	

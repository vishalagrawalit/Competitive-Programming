def min_changes(li):
  change, check = 0, 0
  li_len = len(li)
  if li_len in [0,1]:
    return change
  else:
    check = li[0]
  for i in range(1, len(li)):
    if check >= li[i]:
      li[i] = check +1
      change += 1
      check += 1
    else:
      check = li[i]
  return change

n = int(input())
arr = list(map(int, input().split()))

print(min_changes(arr))
    

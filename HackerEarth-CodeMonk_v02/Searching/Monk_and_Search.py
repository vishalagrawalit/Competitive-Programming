from sys import stdin
 
line_index = -1
lines = stdin.readlines()
 
def get_line():
	global lines, line_index
 
	line_index += 1
	return lines[line_index]
 
def upper_bound(A, target, length):
	lo, high = 0, length + 1
 
	while lo < high:
		mid = (high + lo) >> 1
 
		if A[mid] <= target:
			lo = mid + 1
		else:
			high = mid
 
	return lo
 
def lower_bound(A, target, length):
	lo, high = 0, length + 1
 
	while lo < high:
		mid = (high + lo) >> 1
 
		if A[mid] >= target:
			high = mid
		else:
			lo = mid + 1
 
	return lo
 
 
n = int(get_line())
arr = sorted(list(map(int, get_line().split())))
q = int(get_line())
 
for _ in range(q):
	t, v = map(int, get_line().split())
	if t == 0:
		func = lower_bound
	else:
		func = upper_bound
 
	index = func(arr, v, n - 1)
	print(n - index)

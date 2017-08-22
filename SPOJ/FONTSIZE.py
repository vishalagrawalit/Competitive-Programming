import sys

w, h = map(int, sys.stdin.readline().split())
w /= 2 / 3
words = sys.stdin.readline().split()

def fits(size):
	max_line = h / size
	max_column = w / size

	line = 1
	column = 0
	for word in words:
		column += bool(column) + len(word)
		if column >= max_column:
			line += 1
			column = len(word)
		if line >= max_line:
			return False
	return True

min_size = 0
max_size = w / max(map(len, words))
avg = min_size

while max_size - min_size > .0001:
	avg = (max_size + min_size) / 2
	if fits(avg):
		min_size = avg
	else:
		max_size = avg

print('{:.3f}'.format(avg))
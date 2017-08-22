from math import gcd

for _ in range(int(input())):
	a, b = map(int, input().split())
	
	common = gcd(a, b)
	
	print(b//common, a//common)
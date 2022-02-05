k = int(input())
n, m = [int(i) for i in input().split(" ")]

for _ in range(k):
	x, y = [int(i) for i in input().split(" ")]
	if x == n or y == m:
		print("divisa")
	elif x > n:
		if y > m:
			print("NE")
		else:
			print("SE")
	else:
		if y > m:
			print("NO")
		else:
			print("SO")

n = int(input())

leds = [
	6, # 0
	2, # 1
	5, # 2
	5, # 3
	4, # 4
	5, # 5
	6, # 6
	3, # 7
	7, # 8
	6, # 9
]

for i in range(n):
	soma = sum([leds[int(i)] for i in list(input())])
	print(str(soma) + " leds")
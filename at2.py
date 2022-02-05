n = int(input())

picos = 0
loop = [int(i) for i in input().split(" ")]
for i in range(int(n)):
	anterior = i-1

	if i+1 == len(loop):
		proximo = 0
	else:
		proximo = i+1
	
	if loop[i] > loop[proximo] and loop[i] > loop[anterior]:
		picos += 1
	
	elif loop[i] < loop[proximo] and loop[i] < loop[anterior]:
		picos += 1
	
print(picos)
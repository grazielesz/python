def main():
	N = int(input("insira um número inteiro: "))
	dict = {}
	
	for i in range(1, N+1):
		dict[i] = (i ** 2)
		
	print(dict)
main()

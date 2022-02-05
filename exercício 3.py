def main():
	agenda = {}
	
	while True:
		menu()
		op = input("opção: ")
		
		if op == "1":
			incluir(agenda)
		elif op == "2":
			alterar(agenda)
		elif op == "3":
			excluir(agenda)
		elif op == "4":
			consultar(agenda)
		elif op == "5":
			print(agenda)
			
		else:
			print("programa sendo encerrado...")
			break
			
def incluir(agenda):
	nome = input("nome: ")
	telefone = input("telefone: ")	
	agenda[nome] = telefone
	
def alterar(agenda):
	nome = input("nome: ")
	if nome in agenda:
		novoTEL = input("novo telefone: ")	
		agenda[nome] = novoTEL
	else:
		print("contato inexistente!!")
	
def excluir(agenda):
	nome = input("nome: ")
	if nome in agenda:
		del agenda[nome]
	else:
		print("contato inexistente!!")
		
def consultar(agenda):
	nome = input("nome: ")
	
	if nome in agenda:
		print("telefone:", agenda[nome])
	else:
		print("contato inexistente!!")	
	
	
def menu():
	print("\n\n1 - incluir novo contato")
	print("2 - alterar telefone")
	print("3 - excluir contato")
	print("4 - consultar contato")	
	print("5 - mostrar todos os contatos")

main()

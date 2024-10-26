import os

print("Olá, seja bem vindo ao chatP:version0.1beta ")
#functions
def iniciar_chat ():
	os.system("clear")
	mensagens = []
	nome = input("DIGITE SEU NOME: ")
	while True:
		os.system("clear")
		print("nick: ", nome)
		print("---------------------------------")
		if len(mensagens) > 0:
			for m in mensagens:
				print(m['nome'], "-" , m['texto'])
	
		
		print("---------------------------------")
		
		texto = input("MENSAGEM:  ")
		if texto == "quit":
			break
		
		mensagens.append({
			"nome": nome,
			"texto": texto
			
		})
def iniciar_calculos():
	historico = []
	while True:
		os.system("clear")
		print("BEM VINDO A CALCULADORA!")
		print("1. Adição")
		print("2. Subtração")
		print("3. Divisão")
		print("4. Multiplicação")
		print("5. Histórico")
		print("6. Voltar ao menu principal")
		opc = input("")
		
		if opc == "1":
			while True:				
				os.system("clear")
				print("caso queira voltar digite 'back'")
				v1 = float(input("Digite um numero: "))
				v2 = float(input("Digite outro numero: "))
				resultado = v1 + v2
				print(resultado)
				historico.append(resultado)
				b = input("")
				if b == "back":
					break
		elif opc == "2":
			while True:
				os.system("clear")
				print("caso queira voltar digite 'back'")
				v1 = float(input("Digite um numero: "))
				v2 = float(input("Digite outro numero: "))
				resultado = v1 - v2
				print(resultado)
				b = input("")
			
				if b == "back":
					break
		
			
		elif opc == "5":
			print(historico)
			h = input("")
			
#

while True:
	print("-----------------------")
	print("ESCOLHA 1 OPÇÃO:")
	print("1. Iniciar chat")
	print("2. Iniciar calculadora")
	c = input("")
	
	if c == "1":
		iniciar_chat()
		
	elif c == "2":
		iniciar_calculos()
		
	else:
		os.system("clear")
		print("Opcão invalida!!")

	
			
		
		
		
			

def exibir_mensagem():
    print("Olá Mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome = "Anônimo"): 
    print(f"Seja bem vindo {nome}")

exibir_mensagem()
exibir_mensagem_2(nome="Lilian") #Aqui tem que passar o valor de nome, senao dará erro 
exibir_mensagem() #aqui pode chamar a função sem definir o valor, o valor ja foi passado ao declarar a função 
exibir_mensagem_3(nome="Adriel")
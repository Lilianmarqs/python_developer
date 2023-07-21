def calcular_total(numeros): 
    return sum(numeros)


def retornar_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero + 1 

    return antecessor, sucessor

print(calcular_total([20, 32, 77]))
print(retornar_antecessor_e_sucessor(10))
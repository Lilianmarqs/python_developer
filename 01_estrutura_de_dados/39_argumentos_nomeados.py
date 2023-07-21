#formas de passagem e execução de argumento 

def salvar_carro(marca, modelo, ano, placa): 
    print(f"Carro inserido com sucesso!")

salvar_carro("Fiat", "Palio", 1999, "abc-1243")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="abc-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "abc-1234"})
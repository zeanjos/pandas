import pandas as pd
#Uma tabela no pandas é chamado de DataFrame    
#Series -> 1 coluna

tabela_clientes = pd.read_csv("clientes.csv")
print(tabela_clientes['sexo'])

dicionario_produtos = {"nome": ["Iphone XR", "Samsung A10", "Monitor Mancer"], "preco": [3700, 900, 700], "estoque": [100, 50, 75]}

lista_produtos = [
    {"nome": "iphone", "preco": 5000, "estoque": 100},
    {"nome": "ipad", "preco": 9000, "estoque": 50},
    {"nome": "airpod", "preco": 2000, "estoque": 60}
]


tabela_produtos = pd.DataFrame(lista_produtos)
print(tabela_produtos)
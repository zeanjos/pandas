import pandas as pd
from IPython.display import display
#Uma tabela no pandas é chamado de DataFrame    
#Series -> 1 coluna

tabela_clientes = pd.read_csv("clientes.csv")
display(tabela_clientes)

dicionario_produtos = {"nome": ["Iphone XR", "Samsung A10", "Monitor Mancer"], "preco": [3700, 900, 700], "estoque": [100, 50, 75]}

lista_produtos = [
    {"nome": "iphone", "preco": 5000, "estoque": 100},
    {"nome": "ipad", "preco": 9000, "estoque": 50},
    {"nome": "airpod", "preco": 2000, "estoque": 60}
]


tabela_produtos = pd.DataFrame(lista_produtos)

vendas = pd.read_excel("vendas.xlsx")
display(vendas.shape)

display(vendas.head(10))

display(vendas.describe())

produtos = vendas['produto']

import pandas

dados = {
    "Nome": ["João", "Marta", "Ary", "Matheus", "Michele"],
    "Idade": [51, 37, 23, 24, 33]
}

tabela = pandas.DataFrame(dados)
print(tabela)
import pandas

dados = {
    "Nome": ["João", "Marta", "Ary", "Matheus", "Michele", "Fernando", "Larissa"],
    "Idade": [51, 37, 23, 24, 33, 20, 50],
    "Cidade": ["São Paulo", "Recife", 'Recife', "Recife", "Salvador", "Salvador", "Manaus"]
}

tabela = pandas.DataFrame(dados)
filtro = tabela[tabela["Cidade"] == "Recife"]
print(filtro)
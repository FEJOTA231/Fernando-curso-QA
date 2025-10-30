import requests

integrantes = {
    "Dione": "11633422",
    "Pacheco": "11633010"
}

for nome, cep in integrantes.items():
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        cidade = dados.get("localidade", "Cidade não encontrada")
        print(f"{nome} mora em {cidade}.")
    else: 
        print(f"Não foi possível localizar os dados de {nome}.")
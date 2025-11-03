import requests

estados_frete_gratis = ["AC", "AP", "AM", "PA", "RO", "RR", "TO", "AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]

cep = int(input("Digite o seu CEP: "))
url = f"https://viacep.com.br/ws/{cep}/json/"
resposta = requests.get(url)
if resposta.status_code == 200:
    dados = resposta.json()
    logradouro = dados.get("logradouro", "Logradouro não encontrado")
    bairro = dados.get("bairro", "Bairro não encontrado")
    cidade = dados.get("localidade", "Cidade não encontrada")
    estado = dados.get("uf", "Estado não encontrado")
    
    if estado in estados_frete_gratis:
        print("Seu frete é grátis!")
    else:
        print("Você não está elegível para frete grátis.")
else:
    print("Não foi possível localizar o CEP informado.")     
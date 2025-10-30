perifericos = [ 'teclado', 'mouse', 'monitor', 'mousepad', 'extensor' ]

lista = list(perifericos)
print("Lista:", lista)

lista.append('carregador')
lista.append('pilhas')
print("Nova lista:", lista)

lista.pop(0)
print("Lista com um dado removido:", lista)

lista.pop(-1)
print("Lista sem o último item:", lista)

print("Primeiro item da lista:", lista[0])

print("Quantidade de itens na lista:", len(lista))

pessoa = {"nome": "Fernando", "idade": 20, "altura": 1.8}
print("Nome do dono da lista:", pessoa["nome"])

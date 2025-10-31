palavra = input("Digite uma palavgra: ")
vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
contador = 0

for letra in palavra:
    if letra in vogais:
        contador += 1
        
print(f"O número de vogais na palavra '{palavra}' é {contador}.")

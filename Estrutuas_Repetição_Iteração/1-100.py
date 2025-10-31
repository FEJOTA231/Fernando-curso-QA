numeros = []
for i in range(1, 1001):
    numeros.append(i)

print("Números pares de 1 a 1000:")
for numero in numeros:
    if numero % 2 == 0:
        print(numero)

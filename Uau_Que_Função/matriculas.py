matriculas = input('Digite 5 números de matrículas separados por vírgula: ')
matriculas_lista = matriculas.split(',')

if len(matriculas_lista) != 5:
    print("Por favor, digite exatamente 5 números de matrícula!")
else:
    for matricula in matriculas_lista:
        numero = int(matricula.strip())  
        if numero % 2 == 0:
            print(f"Matrícula {numero}: O SEU TIME É O TIME VERMELHO!")
        else:
            print(f"Matrícula {numero}: O SEU TIME É O TIME AZUL!")
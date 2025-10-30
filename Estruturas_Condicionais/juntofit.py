frequencia = 0

print("=== SISTEMA DE ACESSO JUNTOFIT ===\n")

while True:
    print("\n--- CATRACA DE ACESSO ---")
    entrada = input("Digite 'E' para entrar, 'F' para simular uma falta ou 'S' para sair do programa: ").upper()

    if entrada == 'S':
        print("\nSentimos sua falta :(")
        frequencia = 0

    elif entrada == 'E':
        frequencia += 1

        if frequencia < 21:
            print("VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO")
            print(f"Frequência atual: {frequencia}/21")

        elif frequencia == 21:
            print("UHUU 🎉 AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ!")
            print("Contagem será reiniciada.")
            frequencia = 0  

    elif entrada == 'F':
        if frequencia > 0:
            print("QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.")
        else:
            print("Iniciando nova contagem de frequência.")
        frequencia = 0

    else:
        print("Opção inválida! Digite 'E', 'F' ou 'S'.")
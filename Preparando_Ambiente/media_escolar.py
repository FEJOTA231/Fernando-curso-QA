Nota1 = int(input("Digite a primeira nota: "))
Nota2 = int(input("Digite a segunda nota: "))
Nota3 = int(input("Digite a terceira nota: "))
Nota4 = int(input("Digite a quarta nota: "))
Media = (Nota1 + Nota2 + Nota3 + Nota4) / 4

print(f'Sua média foi de {Media}, você foi {"APROVADO!!!" if Media >= 5 else "REPROVADO!!!"}')
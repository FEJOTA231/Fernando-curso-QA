idade = int(input('Digite a idade de seu pet: '))
nome = str(input('Digite o nome de seu pet: '))
porte = str(input('Digite o porte de seu pet (pequeno, médio, grande): ')).lower()
quantidade = int(input('Digite quantos banhos o pet tomou no último ano: '))

if porte == 'pequeno' or porte == 'médio':
    X = quantidade*45 
elif porte == 'grande':
    X = quantidade*55
if porte != 'pequeno' and porte != 'médio' and porte != 'grande':
    print('Porte inválido. Por favor, insira pequeno, médio ou grande.')
    exit()
    
print(f'O pet {nome} tem {idade} anos, o que equivale a {idade*7} anos humanos. O lucro obtido com os banhos do pet no último ano foi de R$ {X},00.')
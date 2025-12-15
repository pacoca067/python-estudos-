nome = input('digite seu nome: ')

print(f'Olá {nome}, Seja bem-vindo! Agora digite sua idade e peso')

idade = int (input("Idade:"))

if idade>=18:
    print(f'De Maior: {idade}')
else:
    print(f"De menor: {idade}")

peso = float (input('Peso:'))
if peso>=80: 
    print(f'{peso}, Peso pesado:')
else:

    if peso >70:
        print(f'{peso}, Peso Médio:')
    else:
        peso<60
        print(f'{peso}, Peso Leve:')
        
        print(f'Nome:{idade} Idade:{idade}  Peso:{peso}')

        print(f'Seja bem-vindo {nome}, a sua idade é ({idade}) anos e seu peso ({peso}) que massa ')



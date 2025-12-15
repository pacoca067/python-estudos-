nome = input("Digite seu nome:")

print(f"Olá {nome} Me diga sua idade:")

idade=  int (input('Digite sua idade:'))

print(f"idade: {f"{idade}, De maior" if idade>=18 else f"{idade}, De menor"}") 

peso = float (input("Digite seu Peso: "))

print(f'Peso: {peso}')

altura = float(input("Digite sua altura:"))

print( f"Nome : {nome}  Idade :{idade} Peso: {peso} Altura: {altura}")

imc = peso / (altura * altura)

print(f'Seu IMC é: {imc}')

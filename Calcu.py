nome = input("Digite o seu nome:")

nota1 = float(input('digite a sua primeira nota:'))

nota2 = float(input('digite a sua segunda nota:'))

nota3 = float(input('digite a sua terceira nota:'))

media = (nota1 + nota2 + nota3) / 3


if media >=7:
    print(nome, "aprovado")
else:
    if media <=5:
        print(nome, 'Reprovado')
    else: 
        print(nome, 'Recuperação')
while True:
    numero = int(input('Escolha um número ou digite 0 para sair: '))

    if numero == 0:
        print('Programa encerrado.')
        break

    if numero % 2 == 0:
        print('Este número é Par')
    else:
        print('Este número é Ímpar')

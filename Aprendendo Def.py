def verificarSeTrangulo (valor1, valor2, valor3):
    if (valor1+valor2) >= valor3 and (valor2+valor3) >= valor1 and (valor3+valor1) >= valor2:
        return 1
    return 0
if verificarSeTrangulo (1,1,1) == 1:
    print('é um triangulo')
else:
    print('Não é um trangulo')     

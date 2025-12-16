def verificarSeTrangulo (valor1, valor2, valor3):
    if (valor1+valor2) >= valor3 and (valor2+valor3) >= valor1 and (valor3+valor1) >= valor2:
        return 1
    return 0

def defineTipoTriangulo(valor1, valor2,valor3):
    if verificarSeTrangulo(valor1,valor2,valor3) == 1:
        if valor1 == valor2 and valor2 == valor3:
            print('triangulo equilatero')
        else:
            if valor1 != valor2 and valor2 != valor3 and valor1 != valor3:
                print('triangulo escaleno')
            else:
                print('triangulo isosceles')
    else:
        print('Não é triangulo')


lado1 = 30
lado2 = 30
lado3 = 40

defineTipoTriangulo(lado1,lado2,lado3)


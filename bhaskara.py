'''Esse programa vai receber como entrada três valores, o a, b e c, que são as constantes ali da equação de segundo grau
e daí você vai, usando a fórmula de Bhaskara, imprimir as raízes, sendo que tem três casos se delta é menor que zero você vai
dizer que não tem raízes reais, se delta é igual a zero você vai dizer que tem uma raíz real e que é tal, se delta for maior
que zero, você vai dizer que tem duas raízes reais'''

import math

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
delta = ((b.__pow__(2)) - (4 * a * c))
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)
if  delta < 0:
    print('O delta é menor que zero, então a equação de segundo grau não possui raízes')
elif delta == 0:
    print('A equação de segundo grau possui uma raíz real que é {}'.format(x1))
else:
    print('A equação de segundo grau possui duas raízes reais que são {} e {}'.format(x1, x2))




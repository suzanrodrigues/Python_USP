'''Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito
com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".'''


num = int(input('Digite um número: '))

anterior = num % 10
num = num // 10
adjacente = False


while num != 0 and not adjacente:
    atual = num % 10
    if atual == anterior:
        adjacente = True
    else:
        anterior = atual
        num = num // 10

if adjacente == True:
    print('sim')
else:
    print('não')




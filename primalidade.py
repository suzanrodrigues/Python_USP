'''Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo".
Caso contrário, imprima "não primo".'''

numero = int(input('Digite um número: '))

if numero < 2:              # 0 e 1 não são números primos
    print('não primo')
elif numero == 2:
    print('primo')          # 2 é o único número par que é primo
elif numero % 2 == 0:
    print('não primo')      # números pares, com excessão do 2, não são primos
else:
    for i in range(3, numero, 2):
        if numero % i == 0:
            print('não primo')
            break
    else:
        print('primo')



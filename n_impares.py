"""Receba um número inteiro positivo na entrada e imprima os nn primeiros números ímpares naturais."""

n = int(input("Digite o valor de n: "))

impar = 1
tamanho = 0

while True:
    print(impar)
    impar = impar + 2
    tamanho = tamanho + 1
    if tamanho == n:
        break
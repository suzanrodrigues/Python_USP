"""Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída
O que este algoritmo faz é simples:
1 - Pega o último digito de n;
2 - Soma este digito na variável s;
3 - Remove o último dígito do número n;
4 - Volta ao passo 1;"""


n = int(input('Digite um número: '))

s = 0
while n:
    s += n % 10 # Soma `s` ao ultimo numeral de `n`
    n //= 10 # Remove o ultimo numero de `n`
print(s)


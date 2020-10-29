num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))
num3 = int(input('Terceiro numero: '))
lista = [num1, num2, num3]
if num1 < num2 and num2 < num3:
    print('crescente')
else:
    print('não está em ordem crescente')
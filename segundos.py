numero = int(input('Por favor, entre com o número de segundos que deseja: '))

dias = numero // (3600 * 24)
sobra = numero % (3600 * 24)

horas = sobra // 3600
sobra1 = sobra % 3600

minutos = sobra1 // 60
sobra2 = sobra1 % 60

print('{} dias, {} horas, {} minutos e {} segundos.'.format(dias, horas, minutos, sobra2))


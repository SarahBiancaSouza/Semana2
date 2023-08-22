from random import randint
from time import sleep

itens = ('Pedra','Papel','Tesoura')

computador = randint(0,2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')

jogador = int(input('Qual é a sua jogada ?'))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(2)

print('-='  * 11)

print(f'Computador jogou:{itens[computador]}')
print(f'jogador jogou: {itens[jogador]}')
print('-='  * 11)


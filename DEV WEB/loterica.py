import random

tam = 6
numUsuario = [0]*tam   #números do usuário
numSorteio = []        #números do sorteio

i = 0
while i < tam:
    sorteio = random.randint(0, 99)
    if sorteio not in numSorteio:
        numSorteio.append(sorteio)
        i += 1

for i in range(tam):
    numUsuario[i] = int(input(f'Digite seu {i+1}° número: '))

cont = 0
numAcertados = []

for palpite in numUsuario:
    for sorteado in numSorteio:
        if palpite == sorteado:
             numAcertados.append(sorteado)
             #adiciona um elemento ao final da lista
             cont += 1

print('Seus números foram:\n', numUsuario)
print('Os números sorteados foram:\n', numSorteio)

if len(numAcertados) > 0:
    print(f'Você acertou {cont} número(s):\n', numAcertados)
else:
    print('infelizmente você não acertou nenhum número')

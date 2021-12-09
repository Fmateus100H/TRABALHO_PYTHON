from registro import produto

def cadastrar(lista: list) -> list:
  x = 1
  P = produto()
  P.nome = input('Nome do produto: ')
  for i in range(len(lista)):
    if P.nome == lista[i].nome:
      print('Nome existente.')
      x = 0
      break
  if x == 1:
    P.quantia = int(input('Quantidade: '))
    P.preco = float(input('Preço: '))
    lista.append(P)
  return lista


def vender(lista: list) -> list:
  produto = input('Digite o nome do produto: ')
  x = 0
  for i in range(len(lista)):
    if lista[i].nome == produto:
      quantia = int(input('Digite a quantidade a vender: '))
      x = 1
      if lista[i].quantia >= quantia:
        preco_total = quantia * lista[i].preco
        lista[i].quantia -= quantia
        print(f'O valor da venda foi de R${preco_total:.2f}')
      else:
        print('Quantidade indisponível')
  if x == 0:
    print('Nome inexistente.')
  return lista


def abastecer(lista: list) -> list:
  produto = input('Digite o nome do produto: ')
  x = 0
  for i in range(len(lista)):
    if lista[i].nome == produto:
      abastece = int(input('Quanto deseja adicionar? '))
      lista[i].quantia += abastece
      x = 1
      break
  if x == 0:
    print('Nome inexistente.')
  return lista

def atualizar(lista: list) -> list:
  produto = input('Digite o nome do produto: ')
  x = 0
  for i in range(len(lista)):
    if lista[i].nome == produto:
      print(f'Preço atual: R${lista[i].preco:.2f}')
      lista[i].preco = float(input('Digite o novo preço: '))
      x = 1
  if x == 0:
    print('Nome inválido.')
  return lista

def listar(lista: list) -> None:
  for i in range(len(lista)):
    if lista[i].quantia < 10:
      falta = 10 - lista[i].quantia
      print(f'Produto: {lista[i].nome}')
      print(f'falta {falta} unidades para atingir 10 unidades')

    

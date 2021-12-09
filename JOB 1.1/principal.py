from util import ler_arquivo, gravar_arquivo
from opcoes_menu import cadastrar, vender, abastecer, atualizar, listar

nome_arquivo = 'bodega.txt'

def menu():
  menu = '''
==============
     MENU
==============
Escolha uma das opções
(1)Cadastrar novo produto
(2)Vender produto
(3)Abastecer estoque
(4)Atualizar preço
(5)Listar produtos a comprar
'''
  
  print(menu)
  N = int(input())
  return N

def opcoes(N: int, lista: list) -> list:
  if N == 1:
    return cadastrar(lista)
  elif N == 2:
    return vender(lista)
  elif N == 3:
    return abastecer(lista)
  elif N == 4:
    return atualizar(lista)
  elif N == 5:
    listar(lista)
    return lista


lista_produtos = ler_arquivo(nome_arquivo)
while True:
  N = menu()
  lista = opcoes(N, lista_produtos)
  gravar_arquivo(lista, nome_arquivo)

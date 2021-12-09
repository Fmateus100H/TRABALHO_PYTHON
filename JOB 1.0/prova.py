from funcionalidades import ler_arquivo, grava_arquivo
from registros import trabalhador

nome_arquivo = 'inss.txt'
arquivo = open(nome_arquivo, 'a')
arquivo.close()

def menu(listas: list):
  menu = '''
=============
    MENU
=============
(1) Cadastrar trabalhador
(2) Previsão de aposentadoria
(3) Aposentar
(4) Maior aposento
(5) Média salarial dos trabalhadores
(6) Média salarial dos aposentados
'''
  print(menu)
  N = int(input())
  if N == 1:
    return incluir(listas)
  if N == 2:
    prev_aposento(listas)
    return listas
  if N == 3:
    return ver_aposentar(listas)
  if N == 4:
    return maior_aposento(listas)
  if N == 5:
    return media_trabalhadores(listas)
  if N == 6:
    return media_aposentados(listas)

def incluir(listas: list) -> list:
  
  T = trabalhador()
  T.nome = input('Nome do trabalhador: ')
  T.ano_nasc = int(input('Ano de nascimento: '))
  T.salario = float(input('Salário: '))
  T.emprego = input('Emprego: ')
  T.ano_inicio_emp = int(input('Ano do início do emprego: '))
  T.aposento = 'N'
  listas.append(T)

  grava_arquivo(nome_arquivo, listas)
  return listas

def prev_aposento(listas: list) -> None:

  N = input('Digite o nome do cidadão\n')
  
  for i in range(len(listas)):
    if N == listas[i].nome:
      idade = 2021 - listas[i].ano_nasc 
      anos_job = 2021 - listas[i].ano_inicio_emp
      
      if listas[i].emprego == 'Professor' or listas[i].emprego == 'professor':
        if idade >= 60 and anos_job >= 30 and listas[i].aposento == 'N':
          print('cidadão apto a se aposentar')
        elif listas[i].aposento == 'S':
          print(f'{listas[i].nome} já se aposentou')
          
        else:
          falta_idade = 60 - idade
          falta_anos_job = 30 - anos_job
          if falta_idade > 0:
            print(f'{2021 + falta_idade}, falta {falta_idade} anos')
          if falta_anos_job > 0:
            print(f'{2021 + falta_anos_job}, falta {falta_anos_job} anos')

      else:
        if idade >= 65 and anos_job >= 35 and listas[i].aposento == 'N':
          print(f'{listas[i].nome} apto a se aposentar')
        elif listas[i].aposento == 'S':
          print(f'{listas[i].nome} já se aposentou')
          
        else:
          falta_idade = 65 - idade
          falta_anos_job = 35 - anos_job
          if falta_idade > 0:
            print(f'{2021 + falta_idade}, falta {falta_idade} anos')
          if falta_anos_job > 0:
            print(f'{2021 + falta_anos_job}, falta {falta_anos_job} anos')


def ver_aposentar(listas: list) -> list:

  N = input('Digite o nome do cidadão\n')
  
  for i in range(len(listas)):
    if N == listas[i].nome:
      idade = 2021 - listas[i].ano_nasc 
      anos_job = 2021 - listas[i].ano_inicio_emp
      
      if listas[i].emprego == 'Professor' or listas[i].emprego == 'professor':
        if idade >= 60 and anos_job >= 30 and listas[i].aposento == 'N':
          print('cidadão apto a se aposentar')
          listas = aposentar(listas, i)
          
        elif listas[i].aposento == 'S':
          print(f'{listas[i].nome} já se aposentou')
          
        else:
          falta_idade = 60 - idade
          falta_anos_job = 30 - anos_job
          if falta_idade > 0:
            print(f'{2021 + falta_idade}, falta {falta_idade} anos')
          if falta_anos_job > 0:
            print(f'{2021 + falta_anos_job}, falta {falta_anos_job} anos')

      else:
        if idade >= 65 and anos_job >= 35 and listas[i].aposento == 'N':
          print(f'{listas[i].nome} apto a se aposentar')
          listas = aposentar(listas, i)
          
        elif listas[i].aposento == 'S':
          print(f'{listas[i].nome} já se aposentou')
          
        else:
          falta_idade = 65 - idade
          falta_anos_job = 35 - anos_job
          if falta_idade > 0:
            print(f'{2021 + falta_idade}, falta {falta_idade} anos')
          if falta_anos_job > 0:
            print(f'{2021 + falta_anos_job}, falta {falta_anos_job} anos')
               
  return listas

def aposentar(listas: list, i: int) -> list:
  listas[i].aposento = 'S'
  listas[i].salario = listas[i].salario * 0.8
  grava_arquivo(nome_arquivo, listas)
  print(f'{listas[i].nome} foi aposentado com sucesso')
  return listas

def maior_aposento(listas: list) -> None:
  maior = 0
  x = 0
  for i in range(len(listas)):
    if listas[i].aposento == 'S':
      if listas[i].salario > maior:
        maior = listas[i].salario
        x = i
  print(f'O maior aposento é do {listas[x].nome} que é R$ {listas[x].salario:.2f}')
  return listas

def media_trabalhadores(listas: list) -> list:
  cont = 0
  soma = 0
  for i in range(len(listas)):
    if listas[i].aposento == 'N':
      soma += listas[i].salario
      cont += 1
  media = soma / cont
  print(f'A média salarial dos trabalhadores é de R$ {media:.2f}')
  return listas

def media_aposentados(listas: list) -> list:
  cont = 0
  soma = 0
  for i in range(len(listas)):
    if listas[i].aposento != 'N':
      soma += listas[i].salario
      cont += 1
  media = soma / cont
  print(f'A média salarial dos aposentados é de R$ {media:.2f}')
  return listas
    

listas = ler_arquivo(nome_arquivo)
while True:
  listas = menu(listas)

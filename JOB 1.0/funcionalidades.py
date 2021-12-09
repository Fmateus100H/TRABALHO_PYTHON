from registros import trabalhador

def ler_arquivo(nome_arquivo: str) -> list:
  
  leitura = []
  arquivo = open(nome_arquivo, 'r')
  
  for linha in arquivo.readlines():
    linha = linha.replace('\n', '')
    divisao = linha.split('#')
    T = trabalhador()
    T.nome = divisao[0]
    T.ano_nasc = int(divisao[1])
    T.salario = float(divisao[2])
    T.emprego = divisao[3]
    T.ano_inicio_emp = int(divisao[4])
    T.aposento = divisao[5]
    leitura.append(T)
    
  arquivo.close()
  return leitura

def grava_arquivo(nome_arquivo: str, listas: list) -> None:
  arquivo = open(nome_arquivo, 'w')
  for i in range(len(listas)):
    add = f'{listas[i].nome}#{listas[i].ano_nasc}#{listas[i].salario}#{listas[i].emprego}#{listas[i].ano_inicio_emp}#{listas[i].aposento}\n'
    arquivo.write(add)

  arquivo.close()

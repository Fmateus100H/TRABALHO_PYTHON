from registro import produto

def ler_arquivo(nome_arquivo: str) -> list:
  arquivo = open(nome_arquivo, 'r')
  lista = []
  for linha in arquivo.readlines():
    linha = linha.replace('\n', '')
    posicoes = linha.split('#')
    P = produto()
    P.nome = posicoes[0]
    P.quantia = int(posicoes[1])
    P.preco = float(posicoes[2])
    lista.append(P)
  arquivo.close()
  return lista


def gravar_arquivo(lista: list, nome_arquivo: str) -> None:
  arquivo = open(nome_arquivo, 'w')

  for i in range(len(lista)):
    linha = f'{lista[i].nome}#{lista[i].quantia}#{lista[i].preco}\n'
    arquivo.write(linha)
  arquivo.close()

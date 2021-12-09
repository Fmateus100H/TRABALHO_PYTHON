A bodega do seu Zé é o mercadinho mais famoso do bairro. Joãozinho começou a trabalhar na bodega e percebeu que o
controle de estoque ainda era feito em um caderno. Para modernizar a bodega, Joãozinho solicita sua ajuda para desenvolver
um sistema para administrar o estabelecimento.

O sistema deve cadastrar os produtos à venda na bodega com informações como nome do produto, quantidade em estoque e
o preço praticado.

O sistema deve ter as seguintes funcionalidades:

1 - Cadastrar um novo produto: o usuário informa o nome do produto, a quantidade em estoque inicial e o preço que será
praticado. Não aceite que um produto que já possua cadastro, seja cadastrado novamente. Se necessário, retorne uma
mensagem indicando a razão do erro.

2 - Vender um produto: o usuário informa o nome do produto e a quantidade vendida. Dê baixa no estoque e escreva na tela
o valor total da venda. Não aceite a saída de produtos inexistentes e nem quantidades inválidas. Se necessário, retorne uma
mensagem indicando a razão do erro.

3 - Abastecer o estoque de um produto: o usuário informa o nome do produto e a quantidade a ser adicionada ao estoque.
Não aceite que um produto que não tenha sido cadastrado tenha seu estoque abastecido. Se necessário, retome uma
mensagem indicando a razão do erro.

4 - Atualizar preço de um produto: o usuário informa o nome do produto e o novo preço a ser praticado. Não aceite que um
produto que não tenha sido cadastrado tenha seu preço alterado. Se necessário, retorne uma mensagem indicando a razão do
erro.

5 - Listar produtos a comprar: o sistema gera uma lista com todos os produtos que possuam menos de 10 unidades no
estoque e informa quantas unidades devem ser compradas para o estoque de um produto volte a ter 10 unidades.

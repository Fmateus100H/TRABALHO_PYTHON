Joãozinho trabalha na previdência social. Como um bom funcionário, ele se empenha para conseguir dar conta dos cálculos previdenciários de todos os cidadãos de seu país. Entretanto, esta é uma tarefa que demanda muito tempo, por isso, ele solicita a sua ajuda para desenvolver um sistema de previdência social. O sistema deve cadastrar cada trabalhador com informações como nome, ano de nascimento, salário, emprego, ano do início do emprego. O programa deve ser capaz de executar as seguintes funcionalidades: 
 
Cadastrar cidadão -> registra um novo cidadão no banco de dados. 

Previsão de aposentadoria -> informa o nome do cidadão e retorna o ano de aposentadoria mais a diferença de tempo até lá. Caso, ele já esteja aposentado, apenas informe isso. 
Exemplo 1: Previsão para 2030. Faltam 9 anos. 
Exemplo 2: O cidadão já se aposentou. 

Aviso de aposentadoria -> informa o nome do cidadão, se o cidadão estiver apto a se aposentar, aposente-o e calcule seu novo salário. Se o cidadão já estiver aposentado ou não puder se aposentar, informe isto em uma mensagem. 

Informe quem tem a maior aposentadoria -> retorna o nome e o valor da maior aposentadoria. 

Média salarial dos trabalhadores na ativa -> retorna a média salarial dos trabalhadores na ativa. 

Média salarial dos aposentados -> retorna a média salarial dos aposentados. 

Considerações: 
 
Considere que o arquivo 'inss.txt' já foi criado, ou crie um arquivo 'inss.txt' vazio e anexe ao seu código. 
Considere que os cidadãos não gostam de repetir nomes, logo, todos os nomes são diferentes. 
Considere que todo mundo já fez aniversário nesse ano. 
Considere que os cidadãos nunca mudam de emprego. Ele iniciam sua carreira e trabalham até a hora de se aposentar. Seus salários não mudam durante o tempo, pois não há inflação no país do Joãozinho. 
O salário de um aposentado é 80% do salário de um trabalhador da ativa. 
Pelas regras da previdência, todos os cidadão só podem se aposentar quando tiverem 35 anos de emprego e 65 anos de idade. A exceção dessa regra é para professores que podem se aposentar com 30 anos de emprego e 60 anos de idade. 
O uso de um arquivo é obrigatório. Você pode usar funções, criar uma biblioteca, implementar um único programa com todas as funcionalidades ou implementar cada funcionalidade com um programa separado. Você pode incluir mais campos no registro, caso ache necessário.

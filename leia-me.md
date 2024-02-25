# Api com Swagger
Api básica de aprendizado ... 

## Instalações

### Virtualenv
A virtualenv é necessária para separar aplicações de outras e não gerar conflitos de versionamento de pacotes/bibliotecas com versão do python.

### Dependencias
Necessário instalar as dependencias abaixo:
pip install ...
 - flask
 - flaks-script
 - flask-migrate
 - flaks-restx (swagger)
 - sqlacodegen (não instalar, dará conflitos) -  É uma lib muito boa, podemos extrair os modelos do banco de dados apenas com um comando e isso elimina perder tempo escrevendo a mão. Procure pela documentação.


## Arquivo flaksenv
Crie um arquivo `.flaskenv` com ele, não será necessário buscar as informações utilizando o dotenv, ele automaticamente obtem os dados do arquivo e insere na sua aplicação.

Por exemplo: O debug da api flask inicializa como `False` e toda vez que atualizar o código, será necessário parar a aplicação e rodar novamente, se você quer que o reload seja persistente então adicione o seguinte comando `FLASK_DEBUG=True` no arquivo `.flaskenv`.

## Flask Shell
Utilize o flask shell para rodar comandos na sua aplicação com o terminal do python

> $ flask shell

Para criar todas as tabelas no banco de dados, utilize o comando abaixo:
> db.create_all()

para criar as tabelas no banco, importe o modelo e rode o mesmo comando acima

> from app.models import *
> db.create_all()

e pronto, agora as tabelas foram criadas no banco de dados.

## Rodar a aplicação
Para rodar o flask podemos utilizar o comando flask no terminal



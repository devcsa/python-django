## Requisitos

-  Python 3 ou superior - Conferir a versão: python --version
-  Django 5 ou superior - Conferir a versão: django-admin --version
-  MySQL 8 ou superior - Conferir a versão: mysql --version

## Como rodar o projeto baixado

Alterar no arquivo "settings.py" as credenciais do banco de dados.
´´´
'ENGINE': 'django.db.backends.mysql',
'NAME': 'nome-do-banco-de-dados',
'USER': 'usuario-do-banco-de-dados',
'PASSWORD': 'senha-do-usuario-do-banco-de-dados',
'HOST': 'localhost',
'PORT': '3306'
´´´

Executar as migrations para criar as tabelas.
´´´
python manage.py migrate
´´´

Rodar o projeto.
´´´
python manage.py runserver
´´´

Acessar a página padrão criada com Django.
´´´
http://127.0.0.1:8000
´´´

Criar o super usuário.
´´´
python manage.py createsuperuser
´´´
´´´
Username (leave blank to use 'cicer'): admin
Email address: csacicero.1979@gmail.com
Password: csa238515
Password (again): csa238515
´´´

Acessar o sistema administrativo padrão do Django.
´´´
http://127.0.0.1:8000/admin
´´´

Usuário: admin<br>
Senha: csa238515

## Sequencia para criar o projeto

Instalar o Django.
´´´
pip install Django
´´´

Criar o projeto com Django.
´´´
django-admin startproject admin .
´´´

Rodar o projeto.
´´´
python manage.py runserver
´´´

Acessar a página padrão criada com Django.
´´´
http://127.0.0.1:8000
´´´

Instalar o conector MySQL.
´´´
pip install mysqlclient
´´´

Criar a base de dados.
´´´
CREATE DATABASE celke CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
´´´

Alterar no arquivo "settings.py" as credenciais do banco de dados.
´´´
'ENGINE': 'django.db.backends.mysql',
'NAME': 'csa_python',
'USER': 'root',
'PASSWORD': '',
'HOST': 'localhost',
'PORT': '3306'
´´´

Executar as migrations para criar as tabelas.
´´´
python manage.py migrate
´´´

Criar o super usuário.
´´´
python manage.py createsuperuser
´´´
´´´
Username (leave blank to use 'cicer'): admin
Email address: csacicero.1979@gmail.com
Password: csa238515
Password (again): csa238515
´´´

Acessar o sistema administrativo padrão do Django.
´´´
http://127.0.0.1:8000/admin
´´´

## Como usar o GitHub

Inicializar um novo repositorio GIT.
´´´
git init
´´´

Adicionar todos os arquivos modificados na área de preparação.
´´´
git add .
´´´

Commit registra as alterações feitas nos arquivos que foram adicionados na área de preparação.
´´´
git commit -m "Base do projeto"
´´´

Verificar em qual branch está.
´´´
git branch
´´´

Renomear a branch atual no GIT para main.
´´´
git branch -M main
´´´

Adicionar um repositório remoto ao repositório local.
´´´
git remote add origin https://github.com/celkecursos/master-week-python-e-django.git
´´´

Enviar os commits locais para um repositório remoto.
´´´
git push -u origin main
´´´

Remover o arquivo do cache do GIT.
´´´
git rm --cached db.sqlite3
´´´

Remover o diretório do cache do GIT.
´´´
git rm --cached -r admin/**pycache**/
´´´

git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/devcsa/python-django.git
git push -u origin main

git remote add origin https://github.com/devcsa/python-django.git
git branch -M main
git push -u origin main

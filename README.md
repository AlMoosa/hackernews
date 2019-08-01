# This is the project, which scrapped from "kaktus.media".
You can clone this projects from:
`git clone git@github.com:Alymbekov/hackernews.git`

Then you create and activate virtual environment by commands:
`python3 -m venv <name your virtual environment>`
`source <name>/bin/activate`

Create .env file on your project level, and write in it:
`SECRET_KEY='<secret key>`
`DEBUG=True`

This project uses Postgresql, so, create Postgresql database:


`sudo apt-get update`
`sudo apt-get install python3-pip python3-dev libpq-dev postgres postgres-contrib`
`sudo su - postgres`

Enter postgres console:

`psql
CREATE DATABASE hackernews;
CREATE USER hacker WITH PASSWORD 'secretpass';
ALTER ROLE hacker SET client_encoding TO 'utf8';
ALTER ROLE hacker SET default_transaction_isolation TO 'read committed';
ALTER ROLE hacker SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE hackernews TO 'hacker';`

Install requirements for this project by
`pip3 install -r requirements.txt`

Finally, run project with command: `python3 manage.py runserver`






adilet's commits:
pip install -r requirements.txt
sudo apt-get update
<!-- sudo apt-get install python3-pip python3-dev libpq-dev postgres postgres-contrib -->
sudo apt-get install postgresql postgresql-contrib
sudo su - postgres



POSTGRESQL + DJANGO

Установим необходимые библиотеки для работы с бд PostgreSQL

sudo apt-get update
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib

Давайте зайдем в панель postgres под суперюзером

sudo su - postgres


Чтобы перейти в бд PostgreSQL введите следующую команду
psql


Создадим базу данных makers. Каждая бд будет иметь изолированный доступ, что очень важно для безопасности данных

CREATE DATABASE makers;


Каждая команда должна завершаться знаком точки с запятой   ;
Теперь мы создадим пользователя базы данных:
CREATE USER dastan WITH PASSWORD '12345';


Мы устанавливаем кодировку UTF-8, которую ожидает Django. Му устанавливаем default transaction isolation scheme равной "read committed", которая устанавливает защиту. И наконец мы устанавливаем timezone (часовой пояс), в данном случае мы указали, что Django будет использовать UTC:
ALTER ROLE root SET client_encoding TO 'utf8';
ALTER ROLE root SET default_transaction_isolation TO 'read committed';
ALTER ROLE root SET timezone TO 'UTC';


Теперь осталось дать права пользователя на доступ к базе
GRANT ALL PRIVILEGES ON DATABASE makers TO dastan;


Выйдем из бд postgres:
\q


Теперь вернемся к обычному терминалу:
exit

Меняем настройки проекта в файле settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'makers',
        'USER': 'dastan',
        'PASSWORD': '12345',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

Вам нужно указать свои данные пользователя: имя и пароль для бд MySQL.
Теперь можно накатывать миграции и продолжать работать с Django

python3 manage.py migrate

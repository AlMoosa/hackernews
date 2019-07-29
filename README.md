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

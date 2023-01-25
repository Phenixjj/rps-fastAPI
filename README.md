# rps-fastAPI
Welcome to Rock Paper Scissors API game

## Installation using docker
Create docker image in the root folder

<code>docker build -t mdtimage .</code>

Build docker service using docker compose

<code>docker-compose build</code>

Create the service

<code>docker-compose up -d</code>

Go to the API documentation

http://localhost:8008/docs

## Local installation
Python version 3.10

It's better to create a python virtual env using conda or venv

Once your virtual env created

Install python dependencies

<code>pip install -r requirements.txt</code>

Go to the app folder

<code>cd app/</code>

Launch the API using uvicorn

<code>uvicorn main:app --reload</code>

Go to the API documentation

http://127.0.0.1:8000/docs

## Run test
<code>python -m pytest</code>
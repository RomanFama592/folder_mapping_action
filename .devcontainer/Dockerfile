FROM python:3.9-slim-buster

RUN useradd -ms /bin/bash --create-home docker
USER docker

WORKDIR /home/docker

RUN pip install --upgrade pip

COPY Pipfile .

RUN pip install pipenv

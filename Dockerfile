FROM python:3.11.3

WORKDIR /code

COPY . /code

RUN pip install -r /code/requirements.txt

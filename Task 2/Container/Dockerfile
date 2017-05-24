FROM python:3.5

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

ENV NAME World

CMD ["python", "hello_docker.py"]
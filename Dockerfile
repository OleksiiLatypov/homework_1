FROM python:3.10

WORKDIR /smartBot_docker

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]

FROM python:3.10

RUN pip install -U pipenv
RUN pipenv install

COPY . /usr/src/app

WORKDIR usr/src/app/src



CMD ["python", "main.py"]
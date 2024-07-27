FROM python:3.8.5-alpine

RUN pip install --upgrade pip 

COPY .requirements.txt .

COPY . ./app

WORKDIR /app

COPY ./entrypoint.sh /

ENTRYPOINT [ "sh", "entrypoint.sh" ]
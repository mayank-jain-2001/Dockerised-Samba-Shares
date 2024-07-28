FROM ubuntu:latest

RUN apt-get update && apt-get install -y smbclient python3 python3-pip && apt-get clean

EXPOSE 5000

RUN apt install python3-flask -y

RUN pip install pysmb==1.2.9.1 --break-system-packages

COPY app /app
WORKDIR /app

ENV FLASK_ENV=development

CMD ["python3", "app.py"]

FROM ubuntu:latest

RUN apt-get update && apt-get install -y smbclient python3 python3-pip && apt-get clean

EXPOSE 5000

RUN apt install python3-flask -y

COPY app /app
WORKDIR /app

CMD ["python3", "app.py"]

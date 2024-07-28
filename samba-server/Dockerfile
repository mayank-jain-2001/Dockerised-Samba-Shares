FROM ubuntu:latest

RUN apt-get update && apt-get install -y samba python3 python3-pip && apt-get clean

RUN mkdir -p /samba/share
RUN chmod -R 0777 /samba/share

RUN echo "[samba_share]\n\
   path = /samba/share\n\
   read only = no\n\
   browsable = yes\n\
   guest ok = yes\n\
   create mask = 0777\n\
   directory mask = 0777" >> /etc/samba/smb.conf

EXPOSE 139 445 5000

RUN apt install python3-flask -y

COPY app /app
WORKDIR /app

ENV FLASK_ENV=development

CMD ["sh", "-c", "service smbd start && python3 app.py"]
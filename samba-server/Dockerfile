FROM ubuntu:latest

RUN apt-get update && apt-get install -y samba && apt-get clean

RUN mkdir -p /samba/share
RUN chmod -R 0777 /samba/share

RUN echo "[samba_share]\n\
   path = /samba/share\n\
   read only = no\n\
   browsable = yes\n\
   guest ok = yes\n\
   create mask = 0777\n\
   directory mask = 0777" >> /etc/samba/smb.conf

EXPOSE 139 445

CMD ["smbd", "-F", "--no-process-group"]
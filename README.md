# Dockerised Samba File Shares

## How to use this project

### Build the samba server
```
cd samba-server/
docker build -t samba-server .
docker run -d --name samba-server -p 139:139 -p 445:445 -p 5000:5000 samba-server
```

### Build the samba client
```
cd samba-client/
docker build -t samba-client .
docker run -d --name samba-client-1 --link samba-server -p 5001:5000 samba-client-1
```

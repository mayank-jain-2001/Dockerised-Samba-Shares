# Dockerised Samba File Shares

## Aim and Motivation of this project
If you are architecting a Network Attached Storage (NAS) system using Samba file
shares, this project can be a good starting point to do a Proof of Concept (POC)
of your idea.

## How to use this project
Step 1: Clone the repo
```
git clone git@github.com:mayank-jain-2001/Dockerised-Samba-Shares.git
```

Step 2: cd into the repo
```
cd Dockerised-Samba-Shares
```

Step 3: Build the docker image and start the containers. By default, one server and two clients are spinned up, but the configuration can be changed in docker-compose.yml file.
```
docker-compose up --build
```


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

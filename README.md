# Dockerised Samba File Shares

## Aim and Motivation of this project
If you are architecting a Network Attached Storage (NAS) system using Samba file
shares, this project can be a good starting point to do a Proof of Concept (POC)
of your idea.

### Design & Concepts: [Link](https://excalidraw.com/#json=LLO-CaWdcfpTYroKL6_yh,3GCKw8hLGnLsmbe16oBjaQ)


## How to use this project
Step 1: Clone the repo
```bash
git clone git@github.com:mayank-jain-2001/Dockerised-Samba-Shares.git
```

Step 2: cd into the repo
```bash
cd Dockerised-Samba-Shares/
```

Step 3: Build the docker image and start the containers. By default, one server and two clients are spinned up, but the configuration can be changed in docker-compose.yml file.
```bash
docker-compose up --build
```
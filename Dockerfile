FROM ubuntu:22.04

RUN apt update && \
apt -y upgrade && \
apt install -y build-essential libssl-dev libffi-dev python3-dev && \
apt install -y python3-pip && \
apt install -y git && \
apt install -y sqlite3 && \
apt install -y vim

RUN mkdir -p home/tempusr/project && \ 
cd home/tempusr/project && \
git init && \
git clone https://github.com/Pasta-appreciation/first-repo.git && \
cd first-repo && \
pip install -r requirements.txt

EXPOSE 8000


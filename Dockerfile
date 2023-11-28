FROM ubuntu:22.04

RUN apt update && \
apt -y upgrade && \
apt install -y build-essential libssl-dev libffi-dev python3-dev && \
apt install -y python3-pip && \
apt install -y git && \
apt install -y sqlite3 && \
apt install -y vim && \
apt install -y nodejs && \
apt install -y npm && \
apt install -y curl && \
npm install n -g && \
n lts

RUN mkdir -p home/tempusr/ && \ 
cd home/tempusr && \
git init && \
git clone https://github.com/Pasta-appreciation/first-repo.git && \
cd first-repo && \
pip install -r requirements.txt && \
cd project && \
python3 manage.py migrate && \
cd tools && \
npm init -y && npm install tailwindcss autoprefixer clean-css-cli && npx tailwindcss init -p 

EXPOSE 8000


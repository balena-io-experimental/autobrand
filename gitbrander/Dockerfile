FROM balenalib/aarch64-python:3.9-stretch

 RUN echo "Installing dependencies..." && \
    apt-get update && apt-get install -y \
    build-essential \
    git

WORKDIR /usr/src/app

COPY start.sh ./
COPY main.py ./
COPY requirements.txt ./
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade Pillow
RUN pip install -r requirements.txt

COPY colors.json ./
COPY input.txt ./

RUN chmod u+x start.sh

CMD ["sh", "./start.sh"]


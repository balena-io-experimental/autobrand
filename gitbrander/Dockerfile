FROM balenalib/%%BALENA_MACHINE_NAME%%-python:3.9-stretch

 RUN echo "Installing dependencies..." && \
    apt-get update && apt-get install -y \
    build-essential \
    git

WORKDIR /usr/src/app

COPY start.sh ./
COPY input.json input.json
COPY main.py ./
COPY requirements.txt ./

ENV INPUT="/usr/src/app/input.json"
ENV OUTPUT="/output/logo.png"

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade Pillow
RUN pip install -r requirements.txt

RUN chmod u+x start.sh

CMD ["sh", "./start.sh"]
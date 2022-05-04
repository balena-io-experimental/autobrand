FROM balenalib/aarch64-debian-node

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install

COPY start.sh ./
COPY input.json input.json
COPY readmegetter.js ./

ENV INPUT="/usr/src/app/input.json"
ENV OUTPUT="/output/output.json"

RUN chmod u+x start.sh

CMD ["sh", "./start.sh"]
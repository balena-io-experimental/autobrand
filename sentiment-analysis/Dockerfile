FROM balenalib/aarch64-debian-node

WORKDIR /usr/src/app

RUN npm install vader-sentiment

COPY start.sh ./

COPY analyse.js ./

RUN chmod u+x start.sh

CMD ["sh", "./start.sh"]



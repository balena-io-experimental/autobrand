FROM balenalib/aarch64-debian-node

WORKDIR /usr/src/app

RUN npm install color

COPY start.sh ./

COPY colorme.js ./

RUN chmod u+x start.sh

CMD ["sh", "./start.sh"]


# create one color 
# positive vs negative
# conservative vs adventurous

# calculate complimentary color
# calculate contrasting color

# check contrast ratio against white background
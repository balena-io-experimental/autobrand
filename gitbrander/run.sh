#!/bin/bash

docker build -t gitbrander .

docker run --rm -v "$(pwd)"/output:/usr/src/app/output gitbrander
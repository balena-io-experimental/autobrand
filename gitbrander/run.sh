#!/bin/bash

docker build -t gitbrander .

docker run --rm -v "$(pwd)"/output:/output gitbrander
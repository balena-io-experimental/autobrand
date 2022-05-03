#!/bin/bash

docker build -t sentiment-analysis .

docker run --rm -v "$(pwd)"/input:/input -v "$(pwd)"/output:/output sentiment-analysis
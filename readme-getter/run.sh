#!/bin/bash

docker build -t readme-getter .

docker run --rm -v "$(pwd)"/output:/output readme-getter
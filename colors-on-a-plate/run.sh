#!/bin/bash

docker build -t colors-on-a-plate .

docker run --rm -v "$(pwd)"/output:/output colors-on-a-plate
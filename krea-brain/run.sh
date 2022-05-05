#!/bin/bash

docker build -t krea_brain .

docker run --rm -v "$(pwd)"/artifacts:/usr/src/app/artifacts krea_brain
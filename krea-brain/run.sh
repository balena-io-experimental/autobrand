#!/bin/bash

DOCKER_BUILDKIT=1 docker build -t krea_brain .

docker run --rm -v "$(pwd)"/artifacts:/usr/src/app/artifacts krea_brain
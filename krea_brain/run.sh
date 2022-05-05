#!/bin/bash

docker build -t krea_brain .

docker run --rm -v "$(pwd)"/artifacts:/artifacts krea_brain
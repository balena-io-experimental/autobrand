#!/bin/bash

# flask app starts readme-getter with input.json

ROOT=$PWD

echo "Executing readme-getter ..."

cd readme-getter

./run.sh

echo "readme-getter done ..."

# get output.json from readme-getter and feed to sentiment-analysis



cd $ROOT




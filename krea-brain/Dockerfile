FROM balenalib/amd64-ubuntu-python:3.6-bionic-build

# Create a working directory
WORKDIR /usr/src/app

COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

RUN apt update
RUN apt install -y wget gcc-8 unzip libssl1.0.0 software-properties-common
RUN add-apt-repository ppa:ubuntu-toolchain-r/test
RUN apt update
RUN apt-get install -y --only-upgrade libstdc++6


COPY ./meta_context.csv .

COPY ./*.py .
COPY ./models ./models
COPY ./artifacts ./artifacts
COPY ./checkpoint ./checkpoint
 
COPY ./*.sh .
RUN chmod +x ./run.sh
RUN chmod +x ./start.sh

CMD ["sh", "./start.sh"]
#
# basic command
# CMD ["python3", "./krea_brain/text_generator.py"]
#
# sleeping for dev work
# CMD ["sleep", "infinity"]  
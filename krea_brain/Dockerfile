FROM balenalib/amd64-ubuntu-python:3.7-bionic-build

# Create a working directory
WORKDIR /usr/src/app

COPY ./requirements.txt .
COPY ./meta_context.csv .

COPY ./*.py .
COPY ./models ./models
COPY ./artifacts ./artifacts
COPY ./checkpoint ./checkpoint
 
COPY ./*.sh .
RUN chmod +x ./run.sh
RUN chmod +x ./start.sh

RUN pip install -r ./requirements.txt

# CMD ["sh", "./start.sh"]
#
# basic command
# CMD ["python3", "./krea_brain/text_generator.py"]
#
# sleeping for dev work
CMD ["sleep", "infinity"]  
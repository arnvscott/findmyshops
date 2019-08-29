FROM ubuntu:bionic
## MAINTAINER Makina Corpus "contact@makina-corpus.com"

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN apt-get update -qq && apt-get install -y -qq \
    # std libs
    git less nano curl \
    ca-certificates \
    wget unzip build-essential\
    # get the latest python, pip and virtual environment 
    python3 python3-pip python3-venv \     
    # geodjango
    gdal-bin binutils libproj-dev libgdal-dev \
    # install postgresql client (NB. latest postgresql client version on ubuntu is 10, however postgresql server version connecting to on debian Postgresql is 11)
    postgresql-client

# download and install ngrok
RUN wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip && \
    unzip ngrok-stable-linux-amd64.zip -d /usr/local/bin && \
    chmod +x /usr/local/bin/ngrok && \
    rm ngrok-stable-linux-amd64.zip

ENV WORKSP_HOME /workspace
ENV VIRTUAL_ENV ${WORKSP_HOME}/virtualenv
ENV SOURCE_HOME ${WORKSP_HOME}/src

WORKDIR ${SOURCE_HOME}

# Copy source code into the container
COPY . .

# Create virtual environment venv for the application
RUN python3 -m venv $VIRTUAL_ENV

# Change system path so the virtual environment Python executables get run in
# preference over the system Python executables 
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install required python packages
RUN pip3 install -r requirements.txt


CMD ["/bin/bash"]
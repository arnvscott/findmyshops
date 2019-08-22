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
    wget build-essential\
    # get the latest python, pip and virtual environment 
    python3 python3-pip python3-venv \     
    # geodjango
    gdal-bin binutils libproj-dev libgdal-dev 

ENV WORKSP_HOME /workspace
ENV VIRTUAL_ENV ${WORKSP_HOME}/virtualenv
ENV SOURCE_HOME ${WORKSP_HOME}/src

WORKDIR ${SOURCE_HOME}

# Create virtual environment venv for the application
RUN python3 -m venv $VIRTUAL_ENV

# Change system path so the virtual environment Python executables get run in
# preference over the system Python executables 
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt


CMD ["/bin/bash"]
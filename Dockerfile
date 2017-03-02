FROM debian:jessie

RUN mkdir /pygame
RUN apt-get update --fix-missing && apt-get install -y python-pygame python-pip python-dev
RUN useradd -m -U -s /bin/bash pygame


WORKDIR /pygame

ADD . /pygame

RUN pip install -r requirements.txt

USER pygame

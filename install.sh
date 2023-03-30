#!/bin/bash

#update and upgrdae packages
sudo apt update
sudo apt -y upgrade

#install java
sudo apt install default-jre

#install docker.io
sudo apt install docker.io

#install pip
sudo apt install python3-pip

#install pulsar python client
pip install pulsar-client

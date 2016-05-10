#!/usr/bin/env bash
apt-get -qqy update
apt-get -qqy upgrade
apt-get -qqy install build-essential
apt-get -qqy install curl
apt-get -qqy install git
apt-get -qqy install libssl-dev
apt-get -qqy install g++ python3-dev python3-setuptools
apt-get -qqy install wget
apt-get -qqy install ca-certificates libffi-dev

easy_install3 pip
pip install --upgrade setuptools

#install bigchaindb
pip3 install bigchaindb

# install rethinkdb
source /etc/lsb-release && echo "deb http://download.rethinkdb.com/apt $DISTRIB_CODENAME main" | sudo tee /etc/apt/sources.list.d/rethinkdb.list
wget -qO- https://download.rethinkdb.com/apt/pubkey.gpg | sudo apt-key add -
apt-get update
apt-get -qqy install rethinkdb    
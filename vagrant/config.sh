#!/usr/bin/env bash
apt-get -qqy update
apt-get -qqy upgrade
apt-get -qqy install build-essential
apt-get -qqy install curl
apt-get -qqy install git
apt-get -qqy install libssl-dev
apt-get -qqy install python3-pip
apt-get -qqy install wget
apt-get -qqy install ca-certificates libffi-dev
apt-get -qqy install g++ python3-dev
apt-get -qqy install python3-setuptools

easy_install3 pip

#install bigchaindb
wget https://github.com/bigchaindb/bigchaindb/archive/v0.3.0.tar.gz
    tar -xvzf v0.3.0.tar.gz && \
    rm -Rf v0.3.0.tar.gz && \
    cd bigchaindb-0.3.0 && \
    python3 setup.py install && \
rm -rf /var/cache/apk/*

# install rethinkdb
source /etc/lsb-release && echo "deb http://download.rethinkdb.com/apt $DISTRIB_CODENAME main" | sudo tee /etc/apt/sources.list.d/rethinkdb.list
wget -qO- https://download.rethinkdb.com/apt/pubkey.gpg | sudo apt-key add -
apt-get update
apt-get -qqy install rethinkdb    
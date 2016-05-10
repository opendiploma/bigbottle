Run (first time it will start with provisioning):
```text
$ vagrant up
```
Login to virtual machine:
```text
$ vagrant ssh
```
Ones logged in virtual machine, start rethinkdb:
```text
$ rethinkdb
```
Configure bigchaindb in another terminal window:
```text
$ bigchaindb -y configure
```
Run bigchaindb instance:
```text
$ bigchaindb
```

It's more convenient to run rethinkdb using init.d script.

Setup:
```text
sudo cp /etc/rethinkdb/default.conf.sample /etc/rethinkdb/instances.d/instance1.conf
sudo vim /etc/rethinkdb/instances.d/instance1.conf
```
Usage:
```text
sudo /etc/init.d/rethinkdb start
```

Ports on host machine:

8042 - rethinkdb web console
```text
http://localhost:8042/
```
8777 - bigbottle rest api
```text
http://localhost:8777/
```



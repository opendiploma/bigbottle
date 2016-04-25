# bigbottle

[![Join the chat at https://gitter.im/opendiploma/bigbottle](https://badges.gitter.im/opendiploma/bigbottle.svg)](https://gitter.im/opendiploma/bigbottle?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
Rest api for BigchainDB using BottlePy python framework.

Main motivation is to add possibility to access bigchaindb from any kind of server/client what support http calls.
For python server application it's better to use native python driver from Bigchaindb.

It comes together with bottlepy version '0.13-dev'. Normally it should work if you have already bottlepy installed.

After you start bigchaindb instance, run in a folder with bigbottle:
```text
$ python3 -m bottle --debug --reload --bind 0.0.0.0:8777 bigbottle
```
The are 3 methods so far.
```text
GET http://localhost:8777/keys
```
Returns generated private and public keys.

```text
POST http://localhost:8777/store
```
Stores an asset in bigchainDB. Takes 2 parameters: `pub` - public key, `asset` - asset to store (string).

```text
GET http://localhost:8777/exists
```
Checks if asset exists in bigchainDB. Takes 1 parameter: `asset` - asset to check.

Bigbottle is in alpha version. I use it for my prototype. So fill free to join and contribute:)

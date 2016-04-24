from bottle import route, template, request
from bigchaindb import Bigchain, crypto, util

b = Bigchain()


@route('/hello')
def hello():
    return "Hello World!"


@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)


@route('/keys')
def keys():
    testuser1_priv, testuser1_pub = crypto.generate_key_pair()
    return template('priv={{priv}}&pub:{{pub}}', priv=testuser1_priv, pub=testuser1_pub)


@route('/store', method='GET')
def store():
    private_key = request.GET.get('priv', '').strip()
    public_key = request.GET.get('pub', '').strip()
    diploma = request.GET.get('diploma', '').strip()

    digital_asset_payload = {'msg': diploma}

    # a create transaction uses the operation `CREATE` and has no inputs
    tx = b.create_transaction(b.me, public_key, None, 'CREATE', payload=digital_asset_payload)

    # all transactions need to be signed by the user creating the transaction
    tx_signed = b.sign_transaction(tx, b.me_private)

    # write the transaction to the bigchain
    # the transaction will be stored in a backlog where it will be validated,
    # included in a block, and written to the bigchain
    return b.write_transaction(tx_signed)


@route('/check', method='GET')
def check():
    diploma = request.GET.get('diploma', '').strip()

    digital_asset_payload = {'msg': diploma}
    hash = crypto.hash_data(util.serialize(digital_asset_payload))

    transaction = b.get_tx_by_payload_hash(hash)
    if transaction is not None:
        'true'
    return 'false'



    # run(host='localhost', port=8777, debug=True)

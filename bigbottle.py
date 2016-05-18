from bottle import get, request, post, static_file, route
import bigchain_client
import json

user_public_key = '7By7xQPn1gPsqCeAqSJXcLGqukobmJfsGa1ovczTvibh'
user_private_key = '845zJ4tQZUo4jNCBfYzZhWPBrt2Akwi2fptLpWnnE2uW'

univer_public_key = 'ACUTcyq9YzodJRoU2LgTAKe2VXB59KYogvMDB1KLkN5R'
univer_private_key = '8rnGzzC4doGghk3aHe4uw3CLX9xCZhFoakzDWKMZqX9H'


@get('/keys')
def keys():
    user_priv, user_pub = bigchain_client.generate_key_pair()
    return json.dumps({'private': user_priv, 'public': user_pub})


@post('/store')
def store():
    public_key = get_request_param('pub') or user_public_key
    asset = get_request_param('asset')

    digital_asset_payload = get_asset_payload(asset)

    store_result = bigchain_client.store_asset(public_key, digital_asset_payload)

    return json.dumps({'pub': public_key, 'asset': digital_asset_payload, 'transaction': store_result})


@get('/exists')
def exists():
    asset = request.GET.get('asset', '').strip()

    digital_asset_payload = get_asset_payload(asset)
    result, transactions = bigchain_client.exists(digital_asset_payload)

    return json.dumps({'result': result, 'asset': asset, 'transactions': transactions})


@get('/owned')
def get_owned():
    pub = request.GET.get('pub', '').strip() or user_public_key

    transactions = bigchain_client.get_owned_ids(pub)

    return json.dumps(transactions)


@post('/sign')
def sign():
    public_key = get_request_param('pub') or user_public_key
    private_key = get_request_param('priv') or user_private_key
    send_to_key = get_request_param('send_to') or univer_public_key
    tx_id = get_request_param('tx_id')

    tx = {'cid': 0, 'txid': tx_id}

    store_result = bigchain_client.sign_transaction(public_key, private_key, send_to_key, tx)

    return json.dumps({'result': store_result})


@route('/app/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/vagrant/bb/app')


def get_asset_payload(asset):
    return {'asset': asset}


def get_request_param(param_name):
    result = request.forms.get(param_name, '').strip()
    if not result:
        result = request.GET.get(param_name, '').strip()
    return result

# run(host='localhost', port=8777, debug=True)

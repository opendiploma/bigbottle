from bottle import route, request
from bigchaindb import bigchain_client
import json


@route('/keys')
def keys():
    user_priv, user_pub = bigchain_client.generate_key_pair()
    return json.dumps({'private': user_priv, 'public': user_pub})


@route('/store', method='POST')
def store():
    public_key = request.POST.get('pub', '').strip()
    asset = request.POST.get('asset', '').strip()

    digital_asset_payload = {'asset': asset}

    return bigchain_client.store_asset(public_key, digital_asset_payload)


@route('/exists', method='GET')
def exists():
    asset = request.GET.get('asset', '').strip()

    digital_asset_payload = {'asset': asset}
    result = bigchain_client.exists(digital_asset_payload)

    return json.dumps({'result': result})


# run(host='localhost', port=8777, debug=True)

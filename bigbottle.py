from bottle import get, request, post
import bigchain_client
import json


@get('/keys')
def keys():
    user_priv, user_pub = bigchain_client.generate_key_pair()
    return json.dumps({'private': user_priv, 'public': user_pub})


@post('/store')
def store():
    public_key = get_request_param('pub')
    asset = get_request_param('asset')

    digital_asset_payload = get_asset_payload(asset)

    store_result = bigchain_client.store_asset(public_key, digital_asset_payload)

    return json.dumps({'pub': public_key, 'asset': digital_asset_payload, 'result': store_result})


@get('/exists')
def exists():
    asset = request.GET.get('asset', '').strip()

    digital_asset_payload = get_asset_payload(asset)
    result = bigchain_client.exists(digital_asset_payload)

    return json.dumps({'result': result})


def get_asset_payload(asset):
    return {'asset': asset}


def get_request_param(param_name):
    result = request.forms.get(param_name, '').strip()
    if not result:
        result = request.GET.get(param_name, '').strip()
    return result

# run(host='localhost', port=8777, debug=True)

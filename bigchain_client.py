from bigchaindb import Bigchain, crypto, util

b = Bigchain()


def generate_key_pair():
    return crypto.generate_key_pair()


def store_asset(public_key, digital_asset_payload):
    tx = b.create_transaction(b.me, public_key, None, 'CREATE', payload=digital_asset_payload)

    tx_signed = b.sign_transaction(tx, b.me_private)

    return b.write_transaction(tx_signed)


def exists(digital_asset_payload):
    payload_hash = crypto.hash_data(util.serialize(digital_asset_payload))

    transactions = b.get_tx_by_payload_hash(payload_hash)
    result = transactions is not None and len(transactions) > 0

    return result


from bigchaindb import Bigchain, crypto, util

b = Bigchain()


def generate_key_pair():
    return crypto.generate_key_pair()


def store_asset(public_key, digital_asset_payload):
    tx = b.create_transaction(b.me, public_key, None, 'CREATE', payload=digital_asset_payload)

    tx_signed = b.sign_transaction(tx, b.me_private)
    b.write_transaction(tx_signed)

    return tx_signed


def sign_transaction(public_key, private_key, send_to_key, tx_id):
    # Create a transfer transaction
    tx_transfer = b.create_transaction(public_key, send_to_key, tx_id, 'TRANSFER')

    # Sign the transaction
    tx_transfer_signed = b.sign_transaction(tx_transfer, private_key)

    # Write the transaction
    b.write_transaction(tx_transfer_signed)

    return tx_transfer_signed


def exists(digital_asset_payload):
    payload_hash = crypto.hash_data(util.serialize(digital_asset_payload))

    transactions = b.get_tx_by_payload_hash(payload_hash)
    result = transactions is not None and len(transactions) > 0

    return result, transactions


def get_owned_ids(public_key):
# transactions = b.get_owned_ids(public_key)
#
# return transactions
    transactions_ids = b.get_owned_ids(public_key)
    transactions = []

    for tx in transactions_ids:
        full_transaction = b.get_transaction(tx['txid'])
        transactions.append(full_transaction)

    return transactions



# ETH.py
from web3 import Web3
from eth_account import Account
import hashlib
import hmac
import os
w3 = Web3(Web3.HTTPProvider("https://data-seed-prebsc-1-s1.binance.org:8545/"))

class ETH:
    def __init__(self, seed_phrase):
        self.privateKey = self.generate_private_key(seed_phrase)

    # Account.enable_unaudited_hdwallet_features()
        w3.eth.account.enable_unaudited_hdwallet_features()
    def balance(self):
        acc = w3.eth.account.from_key(self.privateKey)
        return w3.eth.get_balance(acc.address)
    def generate_private_key(self, seed_phrase):
        seed_bytes = seed_phrase.encode('utf-8')
        seed = hashlib.sha256(seed_bytes).digest()
        private_key = hmac.new(b'Bitcoin seed', seed, hashlib.sha512).digest()[:32]
        return private_key.hex()
    def address(self):
        acc = w3.eth.account.from_key(self.privateKey)
        return acc.address

    def getPrivateKey(self):
        return self.privateKey

    def send(self, address, amount):
        key = w3.eth.account.from_key(self.privateKey)
        amount = Web3.to_wei(amount, 'ether') 
        tx = {
            'to': address,
            'from': key.address,
            'value': amount,
            'gas': 21000,
            'gasPrice': Web3.to_wei('10', 'gwei'),
            'nonce': w3.eth.get_transaction_count(key.address),
            'chainId': 97
        }
        signed_tx = key.signTransaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(tx_hash)
        return tx_hash

    

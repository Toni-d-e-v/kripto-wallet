# tron.py

from tronpy import Tron
from tronpy.keys import PrivateKey
import base58



class TRON:
    def __init__(self, privateKey):
        self.privateKey = privateKey
        self.tron = Tron()

    def balance(self):
        address = PrivateKey(bytes.fromhex(self.privateKey)).public_key.to_address()
        account = self.tron.get_account(address)
        return account.balance

    def address(self):
        address = PrivateKey(bytes.fromhex(self.privateKey)).public_key.to_address().hex()
        address = base58.b58encode_check(bytes.fromhex(address))
        address = str(address)[2:-1]
        return str(address)
    def getPrivateKey(self):
        return self.privateKey

    def send(self, address, amount):
        from_addr = PrivateKey(bytes.fromhex(self.privateKey)).public_key.to_address()
        tx = self.tron.transaction_builder.send_trx(
            from_addr=from_addr,
            to_addr=address,
            amount=amount * 10**6,  # TRX amount is in SUN (smallest unit)
            memo='',
        )
        signed_tx = tx.sign(PrivateKey(bytes.fromhex(self.privateKey)))
        result = self.tron.trx.send_raw_transaction(signed_tx)
        return result['txid']


def generate_tron():
    private_key = PrivateKey.random().hex()
    return TRON(private_key)

def test():
    tron = generate_tron()
    print("Address: ", tron.address())

    print("Private Key: ", tron.getPrivateKey())



if __name__ == "__main__":
    test()

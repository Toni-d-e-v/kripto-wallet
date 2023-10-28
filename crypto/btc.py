# BTC.py
import bit
from bit import Key, MultiSig, PrivateKey, PrivateKeyTestnet
from bit import wif_to_key
import mnemonic
import bip32utils


class BTCFromSeed:
    def __init__(self, seed_phrase):
        self.seed_phrase = seed_phrase
        self.mnemonic_inst = mnemonic.Mnemonic("english")  # Set the language of the seed phrase

    def generate_btc_from_seed(self):
        if self.mnemonic_inst.check(self.seed_phrase):
            seed = self.mnemonic_inst.to_seed(self.seed_phrase)
            private_key = bip32utils.BIP32Key.fromEntropy(seed)
            print(private_key)
            return BTC(private_key.WalletImportFormat())
        else:
            raise ValueError("Invalid seed phrase")
class BTCFromSeedTest:
    def __init__(self, seed_phrase):
        self.seed_phrase = seed_phrase
        self.mnemonic_inst = mnemonic.Mnemonic("english")  # Set the language of the seed phrase

    def generate_btc_from_seed(self):
        if self.mnemonic_inst.check(self.seed_phrase):
            seed = self.mnemonic_inst.to_seed(self.seed_phrase)
            private_key = bip32utils.BIP32Key.fromEntropy(seed)
            print(private_key)
            return BTCTest(private_key.WalletImportFormat())
        else:
            raise ValueError("Invalid seed phrase")
class BTC:
    def __init__(self, mnemonic):
        self.mnemonic = mnemonic

    def balance(self):
        return Key(self.mnemonic).get_balance('btc')

    def address(self):
        return Key(self.mnemonic).address

    def mnemonic(self):
        return self.mnemonic

    def send(self, address, amount):
        key = Key(self.mnemonic)
        outputs = [(address, amount, 'btc')]
        return key.send(outputs)


class BTCTest:
    def __init__(self, mnemonic):
        self.mnemonic = mnemonic

    def balance(self):
        return PrivateKeyTestnet(self.mnemonic).get_balance('btc')

    def address(self):
        return PrivateKeyTestnet(self.mnemonic).address

    def mnemonic(self):
        return self.mnemonic
    
    def send(self, address, amount):
        key = PrivateKeyTestnet(self.mnemonic)
        outputs = [(address, amount, 'btc')]
        return key.send(outputs)

def generate_btc():
    mnemonic = bit.PrivateKey().to_wif()
    print(mnemonic)
    return BTC(mnemonic)

def generate_btctest():
    mnemonic = bit.PrivateKeyTestnet().to_wif()
    print(mnemonic)
    return BTCTest(mnemonic)


def test():
    btc = generate_btc()
    btctest = generate_btctest()
    print(btc.address())
    print(btctest.address())
    

test()
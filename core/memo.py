from mnemonic import Mnemonic

def create_memo():
    mnemo = Mnemonic("english")
    words = mnemo.generate(strength=256)
    return words

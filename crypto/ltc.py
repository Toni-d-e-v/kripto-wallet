from litecoinutils.setup import setup
from litecoinutils.keys import PrivateKey
from litecoinutils.transactions import Transaction, TxInput, TxOutput

class Litecoin:
    
    def __init__(self, private_key):
        self.private_key = private_key
        setup('mainnet')  # Use 'litecoin-mainnet' for the main Litecoin network

    def balance(self):
        return 0 # todo

    def address(self):
        setup('mainnet')  # Use 'litecoin-mainnet' for the main Litecoin network
        address = PrivateKey(self.private_key).get_public_key().get_segwit_address().to_string()
        return str(address)

    def getPrivateKey(self):
        setup('mainnet')  # Use 'litecoin-mainnet' for the main Litecoin network

        return PrivateKey(self.private_key).to_wif(compressed=True)

    def send(self, address, amount):
        setup('mainnet')  # Use 'litecoin-mainnet' for the main Litecoin network


        from_address = PrivateKey(self.private_key).get_public_key().get_segwit_address().to_string()

        # Create transaction input
        txin = TxInput(prev_tx='previous_tx_hash', prev_index=0)  # Replace with the actual input details

        # Create transaction output
        txout = TxOutput(value=amount, script_pubkey=address.to_script_pub_key())

        # Create the transaction
        tx = Transaction([txin], [txout])

        # Sign the transaction with the private key
        private_key = PrivateKey(self.private_key)
        tx.sign_input(0, private_key)

        # Print the raw transaction
        print("Raw Transaction:", tx.serialize())

        # Broadcast the transaction to the network
        tx.broadcast()

        # Print transaction details
        print("Transaction ID:", tx.get_txid())
        print("Transaction Output:", tx.outputs[0])
        return tx.txid
class LitecoinTest:
    def __init__(self, private_key):
        self.private_key = private_key
        setup('testnet')  # Use 'litecoin-mainnet' for the main Litecoin network

    def balance(self):
        return 0 # todo

    def address(self):
        setup('testnet')  # Use 'litecoin-mainnet' for the main Litecoin network
        address = PrivateKey(self.private_key).get_public_key().get_segwit_address().to_string()
        return str(address)

    def getPrivateKey(self):
        setup('testnet')  # Use 'litecoin-mainnet' for the main Litecoin network

        return PrivateKey(self.private_key).to_wif(compressed=True)

    def send(self, address, amount):
        setup('testnet')  # Use 'litecoin-mainnet' for the main Litecoin network

        from_address = PrivateKey(self.private_key).get_public_key().get_segwit_address().to_string()

        # Get unspent outputs for the address
        unspent_outputs = from_address.get_unspent()

        # Create transaction input
        txin = unspent_outputs[0].to_input()
        # Create transaction output
        txout = TxOutput(value=amount, script_pubkey=address.to_script_pub_key())

        # Create the transaction
        tx = Transaction([txin], [txout])

        # Sign the transaction with the private key
        private_key = PrivateKey(self.private_key)
        tx.sign_input(0, private_key)

        # Print the raw transaction
        print("Raw Transaction:", tx.serialize())

        # Broadcast the transaction to the network
        tx.broadcast()

        # Print transaction details
        print("Transaction ID:", tx.get_txid())
        print("Transaction Output:", tx.outputs[0])
        return tx.txid


def generate_litecoin():
    setup('mainnet')
    private_key = PrivateKey().to_wif()
    return Litecoin(private_key)
def generate_litecoin_test():
    setup('testnet')
    private_key = PrivateKey().to_wif()
    return LitecoinTest(private_key)

def getBothLitecoin():
    return generate_litecoin(), generate_litecoin_test()

def test():
    litecoin = generate_litecoin()
    print(litecoin.address())
    print(litecoin.getPrivateKey())
    print(litecoin.balance())
    ltct = generate_litecoin_test()
    print(ltct.address())
    print(ltct.getPrivateKey())
    print(ltct.balance())
    

if __name__ == "__main__":
    test()

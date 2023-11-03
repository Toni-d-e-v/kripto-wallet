from crypto import btc,eth,ltc,tron






def get_address_balance(symbol,memo):
    print(symbol,memo)
    match symbol:
        case "BTC":
            btc_from_seed = btc.BTCFromSeed(memo)
            btc_instance = btc_from_seed.generate_btc_from_seed()
            return btc_instance.address(),btc_instance.balance()
        case "BTCT":
            btc_from_seed = btc.BTCFromSeedTest(memo)
            btc_instance = btc_from_seed.generate_btc_from_seed()
            return btc_instance.address(),btc_instance.balance()
        case "ETH":
            eth_instance = eth.ETH(memo)
            eth_address =  eth_instance.address()
            eth_balance = eth_instance.balance()
            return eth_address, eth_balance / 1000000000000000000
        case _:
            return "0x"
    return "0x"



def send_crypto(symbol,memo,to,amount):
    print(symbol,memo)
    match symbol:
        case "BTC":
            btc_from_seed = btc.BTCFromSeed(memo)
            btc_instance = btc_from_seed.generate_btc_from_seed()
            return btc_instance.send(to,amount)
        case "BTCT":
            btc_from_seed = btc.BTCFromSeedTest(memo)
            btc_instance = btc_from_seed.generate_btc_from_seed()
            return btc_instance.send(to,amount)
        case "ETH":
            eth_instance = eth.ETH(memo)
            return eth_instance.send(to,amount)
        case _:
            return "0x"
    return "0x"
    

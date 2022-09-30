from blocknative.stream import Stream
import json

global_filters = [{
    # 'status': 'pending-simulation',
}]

network_id_to_name = {
    1: "main",
    3: "ropsten",
    4: "rinkeby",
    5: "goerli",
    42: "kovan",
    100: "xdai",
    56: "bsc-main",
    137: "matic-main",
    250: "fantom-main",
}

api_key = 'a76c4ca7-2600-4f20-b762-375f83300d67'
api_key_1 = '732e577b-5302-4d9a-b1e7-664594ab8663'
stream = Stream(api_key_1, network_id=1, global_filters=global_filters)


try:
    async def txn_handler(txn, unsubscribe):
        # This will only get called with transactions that have status of 'confirmed'
        # This is due to the global filter above
        if txn['status'] in {"confirmed", "pending-simulation"}:
            with open('result.json', 'a') as f:
                resp = json.dumps(txn, indent=4)
                print(txn['status'])
                f.write(resp)
                f.write(',')
        # if txn['status'] in {"confirmed", "pending"}:
        #     resp = json.dumps(txn, indent=4)
        #     if 'internalTransactions' in txn:
        #         print(txn['status'])
        #     with open('./result_internalTransactions.json', 'a') as f:
        #         f.write(resp)
        #         f.write(',')
except Exception as ex:
    print(ex)


# 订阅地址
usdt_address = '0xdAC17F958D2ee523a2206206994597C13D831ec7'
bian = "0x9696f59E4d72E237BE84fFD425DCaD154Bf96976"
hot_address = '0xdac17f958d2ee523a2206206994597c13d831ec7'
ropsten_address = '0xEE01Ed269F136aa148cBc47bD64193fb784Dba4e'
ropsten_address_2 = '0x577B7260cD5331c452650909e359ab30F23f68d0'

# Global filter will apply to all of these subscriptions
# stream.subscribe_address(curve_fi_address, txn_handler)
# stream.subscribe_address(uniswap_v2_address, txn_handler)

# stream.subscribe_address(usdt_address, txn_handler)
# stream.subscribe_address(bian, txn_handler)
stream.subscribe_address(hot_address, txn_handler)

stream.subscribe_address(ropsten_address, txn_handler)
stream.subscribe_address(ropsten_address_2, txn_handler)

# Start the websocket connection and start receiving events!
stream.connect()

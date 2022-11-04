from blocknative.stream import Stream
import json

global_filters = [{
     "status": "confirmed"
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
api_key_2 = 'e7ea526d-bd20-4013-98a0-421a9db2dd93'
api_key_3 = '237c4249-defe-4fc4-91a1-233ea98011e2'
stream = Stream(api_key_3, network_id=1, global_filters=global_filters)


try:
    async def txn_handler(txn, unsubscribe):
        # This will only get called with transactions that have status of 'confirmed'
        # This is due to the global filter above
        with open('contract_result1.json', 'a') as f:
            resp = json.dumps(txn, indent=4)
            print(txn['status'])
            f.write(resp)
            f.write(',')
except Exception as ex:
    print(ex)


# address = "0xEE01Ed269F136aa148cBc47bD64193fb784Dba4e"
# lower_address = address.lower()
# to_address = "0x8F263bCbf3202f0B5F9F36C440871A93F231B7eA"
# stream.subscribe_address(to_address, txn_handler)

hot_address = '0xdac17f958d2ee523a2206206994597c13d831ec7'
#stream.subscribe_address(hot_address, txn_handler)

#stream.subscribe_address(address, txn_handler)
#stream.subscribe_address(lower_address, txn_handler)


contract_address = "0xdac17f958d2ee523a2206206994597c13d831ec7"
stream.subscribe_address(contract_address, txn_handler)

# Start the websocket connection and start receiving events!
stream.connect()




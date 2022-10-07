import json

with open('./result.json', 'r') as f:
    txs = json.loads(f.read())

confirmed = set()
simulation = set()

both_tx = {'0x690532037f5d10651e6db8cba1ce44267144c511861eb9b37d33c8fd44cc0821',
           '0x19a4bd7758e03f395969a7193640d4b2a3c2f2ac9c8e2c17d3bd5ed175c16dfc',
           '0xa8df6b9739c3aad4e1a55452fe34d43cec954744975a3f491f79bbced3dcb070',
           '0xb836d6cee91c76f8bf444849cf2fb8695cf09828a8aa05c91e002dacd9696c6d'}

for tx in txs:
    if tx['hash'] not in both_tx:
        continue

    if tx['status'] == "pending-simulation":
        internal_transactions = tx['internalTransactions']
        print(tx['hash'])
        for inter_tx in internal_transactions:
            contract_call = inter_tx.get('contractCall', {})
            params = contract_call.get('params', {})
            if contract_call.get('methodName', '') == 'transferFrom':
                print('{} ==> {}, {}'.format(params['_from'], params['_to'], params['_value']))
            if contract_call.get('methodName', '') == 'transfer':
                print('{} ==> {}, {}'.format(inter_tx['from'], params['_to'], params['_value']))
        print('===' * 20)
        # print('pending-simulation  hash --> {}'.format(tx['hash']))
        # simulation.add(tx['hash'])
    # if tx['status'] == 'confirmed':
    #     print('confirmed  hash --> {}'.format(tx['hash']))
    #     confirmed.add(tx['hash'])

# print(confirmed & simulation)

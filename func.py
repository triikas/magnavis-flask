import json
import time


# 139 57 478
def numbers():
    with open('numbers.json') as infile:
        data = json.load(infile)
        # 3д 14д 2д
        a, b, c = 259200, 1209600, 172800
        t = time.time()
        contracts_num, client_num, cargo_num = data['contracts_num'], data['client_num'], data['cargo_num']
        if t - contracts_num[1] > a:
            contracts_num[0] = str(int(contracts_num[0])+round((t - contracts_num[1]) // a))
            contracts_num[1] = t
        if t - client_num[1] > b:
            client_num[0] = str(int(client_num[0])+round((t - client_num[1]) // b))
            client_num[1] = t
        if t - cargo_num[1] > c:
            cargo_num[0] = str(int(cargo_num[0])+round((t - cargo_num[1]) // c))
            client_num[1] = t
    with open('numbers.json', 'w') as outfile:
        json.dump({
            "contracts_num": [contracts_num[0], contracts_num[1]],
            "client_num": [client_num[0], contracts_num[1]],
            "cargo_num": [cargo_num[0], contracts_num[1]]
        }, outfile)
    return [contracts_num[0], client_num[0], cargo_num[0]]
# s = numbers()
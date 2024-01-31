import json
import shutil
import time
import os


# 139 57 478
def numbers():
    with open('numbers.json') as infile:
        data = json.load(infile)
        # # 3д 14д 2д
        # a, b, c = 259200, 1209600, 172800
        # t = time.time()
        contracts_num, client_num, cargo_num = data['contracts_num'], data['client_num'], data['cargo_num']
        # if t - contracts_num[1] > a:
        #     contracts_num[0] = str(int(contracts_num[0])+round((t - contracts_num[1]) // a))
        #     contracts_num[1] = t
        # if t - client_num[1] > b:
        #     client_num[0] = str(int(client_num[0])+round((t - client_num[1]) // b))
        #     client_num[1] = t
        # if t - cargo_num[1] > c:
        #     cargo_num[0] = str(int(cargo_num[0])+round((t - cargo_num[1]) // c))
        #     client_num[1] = t
    # with open('numbers.json', 'w') as outfile:
    #     json.dump({
    #         "contracts_num": [contracts_num[0], contracts_num[1]],
    #         "client_num": [client_num[0], contracts_num[1]],
    #         "cargo_num": [cargo_num[0], contracts_num[1]]
    #     }, outfile)
    return [contracts_num[0], client_num[0], cargo_num[0]]


def docs_update():
    root_p = os.path.join(os.getcwd(), 'docs')
    static_p = os.path.join(os.getcwd(), 'static', 'docs')
    root_docs = list(map(lambda t: [os.path.join(root_p, t), t], os.listdir(root_p)))
    static_docs = list(map(lambda t: [os.path.join(static_p, t), t], os.listdir(static_p)))
    if len(static_docs) <= len(root_docs):
        for i in range(len(static_docs)):
            if static_docs[i][1] == root_docs[i][1] and os.path.getmtime(root_docs[i][0]) > os.path.getmtime(static_docs[i][0]):
                os.remove(static_docs[i][0])
                shutil.copy(root_docs[i][0], static_p)
            else:
                for j in range(len(root_docs)):
                    if static_docs[i][1] == root_docs[j][1] and os.path.getmtime(root_docs[j][0]) > os.path.getmtime(static_docs[i][0]):
                        os.remove(static_docs[i][0])
                        shutil.copy(root_docs[j][0], static_p)

from namedlist import namedlist

RPE = namedlist("Paycall", ["buyer", "seller", "key", "amount"])

all_chains = [
    [RPE('a', 'b', 'psig1', 20),
     RPE('b', 'c', 'psig1', 10)],
    [RPE('c', 'd', 'psig1', 5)],

    [RPE('a', 'b', 'psig1', 20)],
    [RPE('b', 'c', 'psig1', 10)],
    [RPE('c', 'd', 'psig1', 5)],
    [RPE('b', 'c', 'psig1', 10)],
    [RPE('c', 'b', 'psig1', 20)],

    [RPE('a', 'b', 'psig2', 50)],
    [RPE('c', 'd', 'psig2', 70), ],
    [
        RPE('a','b', 'psig3', 10),
        RPE('b', 'c', 'psig3', 5)
    ],
    [
        RPE('c','d', 'psig3',4),
        RPE('d', 'e', 'psig3', 3)
    ]

]

# sums = a->b = 20+20 = 40
#       b->c = 10+10+10-20 = 10
#        c->d = 5+5 = 10

KVstore = dict()

for chain in all_chains:
    chain_head_key = chain[0].buyer + chain[0].key
    chain_tail_key = chain[-1].seller + chain[-1].key


    if 'TAIL' + chain_head_key not in KVstore.keys():
        # We can't merge this to what in KVStore - store and expose it
        if 'HEAD' + chain_head_key not in KVstore.keys():
            KVstore['HEAD' + chain_head_key] = chain
    else:
        # merge!
        newchain = KVstore['TAIL' + chain_head_key] + chain
        del KVstore['TAIL' + chain_head_key]
        KVstore['TAIL' + chain[-1].seller + chain[-1].key] = newchain
        KVstore['HEAD' + KVstore[newchain[0]].buyer + KVstore[
            newchain[0]].key] = newchain
        continue
    # now same for head
    if 'HEAD' + chain_tail_key not in KVstore.keys():
        # We can't merge this to what in KVStore - store and expose it
        if 'TAIL' + chain_tail_key not in KVstore.keys():
            KVstore['TAIL' + chain_tail_key + chain[-1].key] = chain
    else:
        # merge!
        newchain = chain + KVstore['HEAD' + chain_tail_key]
        del KVstore['HEAD' + chain_tail_key]
        KVstore['HEAD' + chain_head_key] = newchain
        KVstore['TAIL' + KVstore[newchain[-1]].seller + KVstore[
            newchain[-1]].key] = newchain

# Print all linked lists
for key in KVstore.keys():
    if 'HEAD' in key:
        assembled_chain = []
        for RPEkey in KVstore[key]:
            assembled_chain.append(KVstore[RPEkey])
        print(assembled_chain)

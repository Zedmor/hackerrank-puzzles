from namedlist import namedlist

RPE = namedlist("Paycall", ["buyer", "seller", "key", "amount"])

links = [
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

for chain in links:
    link_head = chain[0].buyer
    link_tail = chain[-1].seller
    link_keys = []
    for RPE in chain:
        try_to_merge = True
        # Let's look for events with same key and same buyer and seller.
        # If found combine events
        link_key = RPE.buyer + RPE.seller + RPE.key
        link_reverse_key = RPE.seller + RPE.buyer + RPE.key
        if link_key not in KVstore.keys():
            if link_reverse_key in KVstore.keys():
                # What to  do now? we found transaction with same buyer and seller and same psig
                # We substracted  it. Should we do it only in case of len of chain = 1 (one transaction)?
                if len(chain) == 1:
                    KVstore[link_reverse_key].amount -= RPE.amount
                    try_to_merge = False
            else:
                KVstore[link_key] = RPE
        else:
            if len(chain) == 1:
                KVstore[link_key].amount += RPE.amount
                try_to_merge = False
                # Not merging
        # need to take care on reverse key here?
        link_keys.append(link_key)

    if try_to_merge:
        if 'TAIL' + link_head + chain[0].key not in KVstore.keys():
            # We can't merge this to what in KVStore - store and expose it
            if 'HEAD' + link_head + chain[0].key not in KVstore.keys():
                KVstore['HEAD' + link_head + chain[0].key] = link_keys
        else:
            # merge!
            newchain = KVstore['TAIL' + link_head + chain[0].key] + link_keys
            del KVstore['TAIL' + link_head + chain[0].key]
            KVstore['TAIL' + chain[-1].seller + chain[-1].key] = newchain
            KVstore['HEAD' + KVstore[newchain[0]].buyer + KVstore[
                newchain[0]].key] = newchain
            continue
        # now same for head
        if 'HEAD' + link_tail + chain[-1].key not in KVstore.keys():
            # We can't merge this to what in KVStore - store and expose it
            if 'TAIL' + link_tail + chain[-1].key not in KVstore.keys():
                KVstore['TAIL' + link_tail + chain[-1].key] = link_keys
        else:
            # merge!
            newchain = link_keys + KVstore['HEAD' + link_tail + chain[-1].key]
            del KVstore['HEAD' + link_tail + chain[-1].key]
            KVstore['HEAD' + chain[0].buyer + chain[0].key] = newchain
            KVstore['TAIL' + KVstore[newchain[-1]].seller + KVstore[
                newchain[-1]].key] = newchain

# Print all linked lists
for key in KVstore.keys():
    if 'HEAD' in key:
        assembled_chain = []
        for RPEkey in KVstore[key]:
            assembled_chain.append(KVstore[RPEkey])
        print(assembled_chain)

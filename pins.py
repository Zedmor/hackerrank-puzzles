def get_pins(observed):
    import itertools
    '''TODO: This is your job, detective!'''
    variants={1:[1,2,4],2:[1,2,5,3],3:[2,3,6],4:[1,4,5,7],5:[2,4,5,6,8],6:[5,6,3,9],7:[4,7,8], 8:[7,5,8,9,0],9:[9,8,6],0:[8,0]}
    result = []
    for number in observed:
        result.append(map(str,variants[int(number)]))
    return [''.join(x) for x in list(itertools.product(*result))]
print (get_pins('11'))
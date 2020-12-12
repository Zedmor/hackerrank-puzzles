import json

import requests


def get_input_output_api(judge, test):
    with open('/home/zedmor/.config/udebug.json') as debug_creds:
        creds = json.load(debug_creds)

    auth = (creds['username'], creds['password'])

    response = requests.get('https://www.udebug.com/input_api/input_list/retrieve.json',
                            auth=auth,
                            params={'judge_alias': judge, 'problem_id': test},
                            headers={'accept': "application/json"})

    return response


# def pytest_generate_tests(metafunc):
#     _, _, judge, test = metafunc.function.__name__.split('_')
#
#     data = get_input_output_api(judge, test)
#
#     inp, out = data['input'], data['output']
#
#     inp = [i.split() for i in inp.split('\n')]
#
#     out = [i for i in out.split('\n')]
#
#     params = zip(inp, out)
#
#     metafunc.parametrize('args, result', params, ids=[str(e) for e in inp])

def create_cases(judge, test, param_type):
    with open(f'{judge}_{test}_{param_type}.txt') as input_file:
        inp = input_file.read().splitlines()

    new_inp = []
    new_case = []
    for line in inp:
        if line == '---':
            new_inp.append(new_case)
            new_case = []
        else:
            new_case.append(line)
    new_inp.append(new_case)
    if len(new_inp) == 1:
        new_inp = new_inp[0]

    return new_inp

def pytest_generate_tests(metafunc):

    _, _, judge, test = metafunc.function.__name__.split('_')

    inp = create_cases(judge, test, 'input')
    out = create_cases(judge, test, 'output')

    params = zip(inp, out)

    metafunc.parametrize('args, result', params, ids=[str(e) for e in inp])

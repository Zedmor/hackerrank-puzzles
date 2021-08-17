def region_services(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])

    result = fib[n - 1]
    if result % 2 == 1:
        result = 'Region'
    elif result % 5 == 0:
        if result % 2 == 1:
            result = 'Region Services'
        else:
            result = 'Services'

    print(f'{fib[-1]}: {result}')

region_services(5)




def skrzat(base, number):
    # start coding!
    result = 0
    if base is 'b':
        for i,digit in enumerate(reversed(number)):
            result += int(digit) * ((-2)**(i+1))
    return result
print(skrzat('b', '11'))
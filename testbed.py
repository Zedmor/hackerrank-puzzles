def mydecorator(msg='Message'):

    def decorated(f):

        def wrapper(*args, **kwargs):
            print('Message is ' + msg)
            print('1')
            z = 'sda'
            f(*args, **kwargs)
            print('2')

        return wrapper

    return decorated

@mydecorator(msg='Hello')
def func(name):
    print(name)

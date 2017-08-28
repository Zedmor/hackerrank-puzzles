def polysum(n,s):
    '''
    :param n:int
    :param s:float or int
    :return:float
    '''
    import math
    area = (0.25*n*s**2)/math.tan(math.pi/n)
    return(round(area+(s*n)**2,4))
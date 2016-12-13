import string
def is_pangram(st):
    atoz=list(string.ascii_letters)
    for i in st:
        if i in str(atoz):
            try:
                atoz.remove(i);atoz.remove(i.swapcase())
            except ValueError:
                pass
    if atoz==[]:return(True)
    else: return(False)
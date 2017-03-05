# concise definition of the Luhn checksum:
#
# "For a card with an even number of digits, double every odd numbered
# digit and subtract 9 if the product is greater than 9. Add up all
# the even digits as well as the doubled-odd digits, and the result
# must be a multiple of 10 or it's not a valid card. If the card has
# an odd number of digits, perform the same addition doubling the even
# numbered digits instead."
#
# for more details see here:
# http://www.merriampark.com/anatomycc.htm
#
# also see the Wikipedia entry, but don't do that unless you really
# want the answer, since it contains working Python code!
#
# Implement the Luhn Checksum algorithm as described above.

# is_luhn_valid takes a credit card number as input and verifies
# whether it is valid or not. If it is valid, it returns True,
# otherwise it returns False.
def is_luhn_valid(n):
    ###Your code here.
    n = str(n)
    if len(n) % 2 == 0:
        additor = 1
    else:
        additor = 0

    gross = 0
    for i, num in enumerate(n):
        if (i+additor) % 2 == 1:
            result = int(num) *2
            if result > 9:
                result -= 9
        else:
            result = int(num)
        gross += result
    return gross % 10 == 0

n = 4147400144370598
print(is_luhn_valid(n))
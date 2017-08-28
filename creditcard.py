# # Test Case 1:
balance = 3329
annualInterestRate = 0.2
epsilon=0.05

def yearBal(balance,annualInterestRate,payment):
    for i in range(12):
        #balance-=balance*monthlyPaymentRate
        balance -= payment
        balance += balance * (annualInterestRate / 12)

        #print(balance)
    return(balance)

lb = 0
hb = balance
payment = balance/2
while abs(yearBal(balance,annualInterestRate,payment)) > epsilon:
    if yearBal(balance,annualInterestRate,payment) > epsilon: lb=payment; payment = payment+(hb-lb)/2
    else: hb=payment; payment = payment-(hb-lb)/2
print('Lowest Payment:',int(payment),2)


#
# # Result Your Code Should Generate Below:
# Remaining
# balance: 31.38
#
# # To make sure you are doing calculation correctly, this is the
# # remaining balance you should be getting at each month for this example
# Month 1 Remaining balance: 40.99
# Month 2 Remaining balance: 40.01
# Month 3 Remaining balance: 39.05
# Month 4 Remaining balance: 38.11
# Month 5 Remaining balance: 37.2
# Month 6 Remaining balance: 36.3
# Month 7 Remaining balance: 35.43
# Month 8 Remaining balance: 34.58
# Month 9 Remaining balance: 33.75
# Month 10 Remaining balance: 32.94
# Month 11 Remaining balance: 32.15
# Month 12 Remaining balance: 31.38
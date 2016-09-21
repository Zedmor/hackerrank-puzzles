#binominal distr

pb = 0.12
def fac(x):
    fact = 1
    for i in range (1,x+1):
        fact*=i
    return(fact)

def binom(x,n,p):
    return (fac(n)/(fac(n-x)*fac(x))*(p**x)*(1-p)**(n-x))

sump=0
for i in range (3):
 sump+=binom(i,10,pb)
print(round(sump,3))


sump=0
for i in range (2,11):
 sump+=binom(i,10,pb)
print(round(sump,3))

p=1/3

print(round(((1-p)**4)*p,3))



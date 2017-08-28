def fibonacci(n,pr_n=1):
    if n in [0, 1]:
        return n
    #print(n,pr_n)
    return fibonacci(n - 1,n) + pr_n

print([fibonacci(z) for z in range(100)])
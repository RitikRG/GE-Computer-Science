def checkPrime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def primeTillN(n):
    primesList = []

    for i in range(2,n):
        if checkPrime(i):
            primesList.append(i)

    return primesList

def nPrimes(n):
    primesList = []
    start=2
    while len(primesList)!=n :
        if checkPrime(start) :
            primesList.append(start)
        start+=1
    return primesList


n = eval(input('Enter the value of n: '))
print(checkPrime(n))
print(primeTillN(n))
print(nPrimes(n))

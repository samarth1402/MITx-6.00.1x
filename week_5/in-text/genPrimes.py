def checkPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def genPrimes():
    yield 2 #the first prime number
    i = 3
    while True:
        if checkPrime(i):
            yield i
        i +=  2




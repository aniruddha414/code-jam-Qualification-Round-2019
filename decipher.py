t = int(input())
testCases = []
for i in range(0,t):
    input1 = list(map(int, input().strip().split()))
    maxlimit = input1[0]
    noOfPrimes = input1[1]
    listOfNums = list(map(int, input().strip().split()))
    testCases.append([maxlimit,noOfPrimes,listOfNums])

def factorize(number):
    factors = []
    for i in range(2,number):
        if (number % i == 0):
            factors.append(i)
            factors.append(number//i)
            break
    return factors        

def decipher(listOfNumbers):
    text = ""
    alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    primes = [] # list of prime numbers
    listOfFactors = []
    c = 0
    for l in listOfNumbers:
        factors = factorize(l)
        listOfFactors.append(factors)
        if c == 0:
            primes.append(factors[0])
            primes.append(factors[1])
        elif factors[0] not in primes:
            primes.append(factors[0])
        elif factors[1] not in primes:
            primes.append(factors[1])
        c += 1    
    
    primes.sort()
    encoding = {}
    count = 0
    for p in primes:
        encoding[p] = alphabets[count]
        count += 1
    count = 0
    for facs in listOfFactors:
        if count == 0:
            text += encoding[facs[0]] + encoding[facs[1]]
        else:
            prevFacs = listOfFactors[count-1]
            for f in facs:
                if f not in prevFacs:
                    text += encoding[f]   
        count += 1                         
    return text

c = 1
for test in testCases:
    result = decipher(test[2])
    print("Case #"+str(c)+": "+result)
    c += 1
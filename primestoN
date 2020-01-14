#Prime numbers up to n using sieve of Eratosthenes

import list2String

def popNums(n, theList):
    for i in range(0, n+1):
        theList.append(False)

    return theList
    
def sievePrimes(theList):
    p = 2

    for j in range(2, len(theList)+1):
        for i in range (2*j, len(theList), j):
            if i == 4:
                print()
            theList[i] = True

def buildPrimeList(theList):
    primeList = []
    for i in range(2, len(theList)):
        if theList[i] == False:
            primeList.append(i)
    return primeList
    
numList = []
numList = popNums(10000, numList)
sievePrimes(numList)
primeList = buildPrimeList(numList)

print(list2String.list2string(primeList))

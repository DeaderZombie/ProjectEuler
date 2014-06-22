from helper import isPrime

def getLPFactor(n):
	currentValue = n
	startingPrime = 2
	while isPrime(currentValue) != True:
		if isPrime(startingPrime) == True:
			while currentValue%startingPrime == 0:
				currentValue = currentValue/startingPrime
		startingPrime += 1
	return currentValue








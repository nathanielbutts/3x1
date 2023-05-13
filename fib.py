import sys

fib = int(sys.argv[1])

def collatz(num):

    x = 0
    while num != 1:
        if num%2 == 0:
            num = num/2
        else:
            num = 3*num+1
        x += 1
    return x

# Python3 implementation of the approach
import math

# Function that returns True if n
# is prime else returns False
def isPrime(n):
	
	# Corner cases
	if(n <= 1):
		return False
	if(n <= 3):
		return True
	
	# This is checked so that we can skip
	# middle five numbers in below loop
	if(n % 2 == 0 or n % 3 == 0):
		return False
	
	for i in range(5,int(math.sqrt(n) + 1), 6):
		if(n % i == 0 or n % (i + 2) == 0):
			return False
	
	return True

# Function to return the smallest
# prime number greater than N
def nextPrime(N):

	# Base case
	if (N <= 1):
		return 2

	prime = N
	found = False

	# Loop continuously until isPrime returns
	# True for a number greater than n
	while(not found):
		prime = prime + 1

		if(isPrime(prime) == True):
			found = True

	return prime

def write_file(item):      
    with open(filename, 'a') as f:
        f.write(item)
        f.close()

y = 0

#primes = input("How many powers of 10? ")
#primes = int(arg)

print(collatz(fib))

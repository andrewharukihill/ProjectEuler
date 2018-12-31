#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

import time

def isPrime(num):
	if num % 2 == 0 and num > 2:
		return False
	prime = True
	lim = int(num**0.5) + 1
	for i in range(3, lim, 2):
		if (num % i ==0):
			prime = False
			break
	return prime

def main():
	start_time = time.time()

	limit = 2000000

	sum = 0
	for i in range(2,limit):
		if (isPrime(i)):
			sum += i

	print("\nThe sum of all primes below " + str(limit) + " is " + str(sum))

	

	elapsed_time = time.time() - start_time
	print("\nTime elapsed: " + str(elapsed_time))

main()
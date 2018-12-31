#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

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


import time

def main():
	start_time = time.time()

	lim_num = 600851475143
	largest = 0
	
	for i in range(1,int(lim_num**0.5) + 1,2):
		if (isPrime(i) and lim_num % i == 0):
			largest = i

	print("The largest prime factor of " + str(lim_num) + " is " + str(largest))

	elapsed_time = time.time() - start_time
	print("\nTime elapsed: " + str(elapsed_time))

main()
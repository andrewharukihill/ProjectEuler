import time

def isPrime(num):
	if num % 2 == 0 and num > 2:
		return False
	prime = True
	for i in range(2, int((num**0.5)) + 1):
		if (num % i ==0):
			prime = False
			break
	return prime

def main():
	start_time = time.time()

	prime_list = []
	num = 2
	while(len(prime_list) < 10001):

		if (isPrime(num)):
			prime_list.append(num)
		num += 1
	print(prime_list[-1])
	

	elapsed_time = time.time() - start_time
	print("\nTime elapsed: " + str(elapsed_time))

main()
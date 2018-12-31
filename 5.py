# EulerQ5.py

# Time elapsed 83.544 sec

import time

def main():
	start_time = time.time()

	notFound = True
	num = 2520

	while(notFound):
		divisible = True
		for i in range(1,21):
			if (num % i != 0):
				divisible = False
				break
		if (divisible):
			print("The number is " + str(num))
			notFound = False
		if (num % 1000):
			print(num)
		num += 20
	

	elapsed_time = time.time() - start_time
	print("\nTime elapsed: " + str(elapsed_time))

main()
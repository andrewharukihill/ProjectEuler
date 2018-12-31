# 1.py

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
import time

def main():
	start_time = time.time()

	sum = 0
	num = 3
	while (num < 1000):
		if (num % 3 == 0 or num % 5 == 0):
			sum += num
		num += 1
	print (sum)

	elapsed_time = time.time() - start_time
	print("\nTime elapsed: " + str(elapsed_time))

main()
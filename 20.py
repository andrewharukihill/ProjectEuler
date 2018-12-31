
# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!


import time

def sumDigits(num):
	if(num == 0):
		return 0
	else:
		return num%10 + sumDigits(num//10)

def main():
	start_time = time.time()

	num = 1

	for i in range(1, 101):
		num = num*i

	sum = sumDigits(num)
	print("The sum of the digits of 100! is " + str(sum))

	elapsed_time = time.time() - start_time
	print("\nTime elapsed: " + str(elapsed_time))

main()
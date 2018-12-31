# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000?

import time

def sumDigits(num):
	if (num == 0):
		return 0
	else:
		return (num%10) + sumDigits(num//10)


def main():
	start_time = time.time()
	num = 2**1000
	
	sum = sumDigits(num)
	print("The sum of the digits of 2^1000 is " + str(sum))

	elapsed_time = time.time() - start_time
	print("\nTime elapsed: " + str(elapsed_time))

main()
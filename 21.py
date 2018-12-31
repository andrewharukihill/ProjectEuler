#Let d(n) be defined as the sum of proper divisors of n (numbers 
#less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable 
#pair and each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 
#44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 
#1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.



import time
import math

def sumDivisors(num):
	sum = 0
	for i in range(1, num//2):
		if (num % i == 0):
			sum += num
	return sum

def main():
	start_time = time.time()

	sum = 0
	for i in range(0, 100):
		amic_num = sumDivisors(sumDivisors(i))
		if (i == amic_num):
			sum += i
			sum += amic_num
	print("The sum of all amicable numbers under 10000 is: " + str(sum))

	

	elapsed_time = time.time() - start_time
	print("\nTime elapsed: " + str(elapsed_time))

main()
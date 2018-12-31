# The Fibonacci sequence is defined by the recurrence relation:

#Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#Hence the first 12 terms will be:

#F1 = 1
#F2 = 1
#F3 = 2
#F4 = 3
#F5 = 5
#F6 = 8
#F7 = 13
#F8 = 21
#F9 = 34
#F10 = 55
#F11 = 89
#F12 = 144
#The 12th term, F12, is the first term to contain three digits.

#What is the index of the first term in the Fibonacci sequence to contain #
#1000 digits?

import time

def numDigits(num):
	num = str(num)
	return len(num)

def main():
	start_time = time.time()

	fib_list = [0,1,1]
	idx = 3
	fib_num = 0

	while(numDigits(fib_num) < 1000):
		fib_num = fib_list[-1] + fib_list[-2]
		fib_list.append(fib_num)
		idx += 1

	print("The index of the first term in the Fibonacci sequence to contain 1000 digits is " + str(idx - 1))
	

	elapsed_time = time.time() - start_time
	print("\nTime elapsed: " + str(elapsed_time))

main()
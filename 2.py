#Each new term in the Fibonacci sequence is generated by adding the 
#previous two terms. By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

import time

def main():
	start_time = time.time()

	fib = [1,2]
	num = 2
	sum = 2
	while (num < 4000000):
		new_fib = fib[-1] + fib[-2]
		fib.append(new_fib)
		if(new_fib % 2 ==0):
			sum += new_fib
		num = new_fib

	print(sum)

	elapsed_time = time.time() - start_time
	print("\nTime elapsed: " + str(elapsed_time))

main()
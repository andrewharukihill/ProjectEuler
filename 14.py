# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) 
#contains 10 terms. Although it has not been proved yet (Collatz Problem), 
#it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

import time

def collatz(num):
	num_chain = 0
	while(num > 1):
		if (num % 2 == 0):
			num = num/2
		else:
			num = 3*num + 1
		num_chain += 1
	return num_chain

def main():
	start_time = time.time()

	lim_num = 1000000
	longest_chain = 0
	longest_chain_num = 0

	for i in range(1, lim_num + 1):
		num_chain = collatz(i)
		if (num_chain > longest_chain):
			longest_chain = num_chain
			longest_chain_num = i
	
	print("The number with the longest Collatz chain from 1 to " + str(lim_num) + " is " +
	str(longest_chain_num) + " and it has " + str(longest_chain) + " chains")

	elapsed_time = time.time() - start_time
	print("\nTime elapsed: " + str(elapsed_time))

main()
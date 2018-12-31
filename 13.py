
# Work out the first ten digits of the sum of the following 
# one-hundred 50-digit numbers.

import time

def main():
	start_time = time.time()

	file = "13.txt"
	in_file = open(file, "r")

	sum = 0
	for line in in_file:
		line = line.strip()
		line = int(line)
		sum += line

	sum = str(sum)
	first_ten = sum[0:10]
	print("The first ten digits of the sum are " + first_ten)


	

	elapsed_time = time.time() - start_time
	print("\nTime elapsed: " + str(elapsed_time))

main()
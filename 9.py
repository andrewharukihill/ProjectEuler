#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.


import time

def main():
	start_time = time.time()

	limit_num = 1000

	found_nums = False

	# a cannot be larger than one-third the limit number - 1
	for a in range(1,limit_num//3 -1):

	# b cannot be smaller than a + 1 and cannot be larger than one-third
	# the limit number
		for b in range(a + 1,limit_num //2):

	# Calculate c and check if a^2 + b^2 = c^2
			c = limit_num - a - b
			if (a**2 + b**2 == c**2):
				print("a = " + str(a) + "\nb = " + str(b) + "\nc = " + str(c))
				print("Those numbers' product is " + str(a*b*c))
				found_nums = True

	if (not found_nums):
		print("There are no numbers that fit the constraints")

	

	elapsed_time = time.time() - start_time
	print("\nTime elapsed: " + str(elapsed_time))

main()
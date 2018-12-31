import time

def reverse(num):
	num = str(num)[::-1]
	return int(num)

def lychrel(num, iteration):
	if (iteration==50):
		return 1
	else:
		rev = reverse(num)
		if (num == rev and iteration != 0):
			return 0
		else:
			return lychrel(num+rev, iteration + 1)

def main():
	start_time = time.time()

	range_lim = 100000
	out_sum = 0
	for i in range(1,range_lim):
		out_sum += lychrel(i, 0)
	print("There are " + str(out_sum) + " Lychrel numbers from 1 to " + str(range_lim))
	
	elapsed_time = time.time() - start_time
	print("\nTime elapsed: " + str(elapsed_time))

main()
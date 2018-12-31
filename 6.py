import time

def main():
	start_time = time.time()

	sum_sq = 100*(101)*(201)/6
	sq_sum = (100*(101)/2)**2
	
	diff = sq_sum - sum_sq
	print("Difference: " + str(diff))	

	elapsed_time = time.time() - start_time
	print("\nTime elapsed: " + str(elapsed_time))

main()
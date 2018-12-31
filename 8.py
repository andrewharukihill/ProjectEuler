import time

def main():
	start_time = time.time()

	#read file

	num_str = ""
	file = "8.txt"
	in_file = open(file, "r")
	for line in in_file:
		line = line.strip()
		num_str += line

	#input file into an array and convert str to int
	num = []
	for i in range(len(num_str)):
		num.append(int(num_str[i]))

	idx = 0
	largest = 0
	while(idx < len(num) - 12):
		if (num[idx]*num[idx + 1]*num[idx + 2]*num[idx + 3]*num[idx+4]*num[idx + 5]*num[idx + 6]*num[idx + 7]*num[idx + 8]*num[idx+9]*num[idx + 10]*num[idx + 11]*num[idx + 12] > largest):
			largest = num[idx]*num[idx + 1]*num[idx + 2]*num[idx + 3]*num[idx+4]*num[idx + 5]*num[idx + 6]*num[idx + 7]*num[idx + 8]*num[idx+9]*num[idx + 10]*num[idx + 11]*num[idx + 12]
	
		idx += 1
	print("The largest product of thirteen adjacent digits is: " + str(largest))

	elapsed_time = time.time() - start_time
	print("\nTime elapsed: " + str(elapsed_time))

main()
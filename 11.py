# In the 20×20 grid below, four numbers along a diagonal line have been 
# marked in red.

# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

# What is the greatest product of four adjacent numbers in the same 
# direction (up, down, left, right, or diagonally) in the 20×20 grid?

import time


def main():
	start_time = time.time()

	grid = []

	file = "11.txt"
	in_file = open(file, "r")
	for line in in_file:
		line = line.strip()
		line = line.split(" ")
		grid.append(line)

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			grid[i][j] = int(grid[i][j])

	max_prod = 0
	for i in range(len(grid)):
		for j in range(len(grid)):
		#Check up
			if (j > 2):
				prod = grid[i][j]*grid[i][j-1]*grid[i][j-2]*grid[i][j-3]
				if (prod > max_prod):
					max_prod = prod
		#Check left
			if (i > 2):
				prod = grid[i][j]*grid[i-1][j]*grid[i-2][j]*grid[i-3][j]
				if (prod > max_prod):
					max_prod = prod
		#Check right
			if (i < 17):
				prod = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
				if (prod > max_prod):
					max_prod = prod
		#Check down
			if (j <17):
				prod = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
				if (prod > max_prod):
					max_prod = prod
		#Check down-right diagonal
			if(i < 17 and j < 17):
				prod = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
				if (prod > max_prod):
					max_prod = prod
		#Check down-left diagonal
			if(i> 2 and j < 17):
				prod = grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3]
				if (prod > max_prod):
					max_prod = prod
	print("The max product is " + str(max_prod))




	elapsed_time = time.time() - start_time
	print("\nTime elapsed: " + str(elapsed_time))

main()
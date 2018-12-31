#By starting at the top of the triangle below and moving to adjacent 
#numbers on the row below, the maximum total from top to bottom is 23.

#3
#7 4
#2 4 6
#8 5 9 3

#That is, 3 + 7 + 4 + 9 = 23.

#Find the maximum total from top to bottom in triangle.txt 
#(right click and 'Save Link/Target As...'), a 15K text file 
#containing a triangle with one-hundred rows.

#NOTE: This is a much more difficult version of Problem 18. It is not 
#possible to try every route to solve this problem, as there are 299 
#altogether! If you could check one trillion (1012) routes every second 
#it would take over twenty billion years to check them all. There is an 
#efficient algorithm to solve it. ;o)

import time

def maxPath(triangle):
	for i in range(len(triangle) -1, -1, -1):
		if (i == 0):
			print("The max path-sum is " + str(triangle[0]))
		else:
			for j in range(0, len(triangle[i]) - 1):
				if (triangle[i][j] > triangle[i][j+1]):
					triangle[i-1][j] += triangle[i][j]
				else:
					triangle[i-1][j] += triangle[i][j+1]

def main():
	start_time = time.time()

	file = "67.txt"
	in_file = open(file, "r")

	triangle = []

	for line in in_file:
		line = line.strip()
		line = line.split()
		triangle.append(line)

	for i in range(len(triangle)):
		for j in range(len(triangle[i])):
			triangle[i][j] = int(triangle[i][j])

	maxPath(triangle)

	elapsed_time = time.time() - start_time
	print("\nTime elapsed: " + str(elapsed_time))

main()
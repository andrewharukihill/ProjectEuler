#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

import time

def isPalindrome(num):
	num = str(num)
	rev_num = reverseStr(num)
	return num == rev_num

def reverseStr(str):
	if len(str) <= 1:
		return str

	return reverseStr(str[1:]) + str[0]

def main():
	start_time = time.time()
	largest = 0
	for i in range(1,1000):
		for j in range(1,1000):
			if (isPalindrome(i*j) and i*j > largest):
				largest = i*j
				
	print("The largest palindrome is " + str(largest))

	elapsed_time = time.time() - start_time
	print("\nTime elapsed: " + str(elapsed_time))

main()
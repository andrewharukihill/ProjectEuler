#Using names.txt (right click and 'Save Link/Target As...'), a 46K text 
#file containing over five-thousand first names, begin by sorting it 
#into alphabetical order. Then working out the alphabetical value for
#each name, multiply this value by its alphabetical position in the list 
#to obtain a name score.

#For example, when the list is sorted into alphabetical order, COLIN, 
#which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
#So, COLIN would obtain a score of 938 × 53 = 49714.

#What is the total of all the name scores in the file?

import time

def firstBigger(a,b):
	if (len(a) > len(b)):
		idx = 0
		notDone = True
		while (idx < len(b) and notDone):
			if (ord(a[idx]) < ord(b[idx])):
				notDone = False
				return True
			elif(ord(a[idx])) > ord(b[idx]):
				notDone = False
				return False
			idx += 1 
		return False
	else:
		idx = 0
		notDone = True
		while (idx < len(a) and notDone):
			if (ord(a[idx]) < ord(b[idx])):
				notDone = False
				return True
			elif(ord(a[idx])) > ord(b[idx]):
				notDone = False
				return False
			idx += 1 
		return True

def insert(list, idx, num):
		pos = idx - 1
		while(pos >= 0 and firstBigger(num,list[pos])):
			list[pos + 1] = list[pos]
			pos = pos - 1
		list[pos + 1] = num

def insertionSort(list):
	for i in range(len(list)):
		insert(list, i, list[i])

def getScore(string):
	score = 0
	for i in range(len(string)):
		score += ord(string[i]) - 64
	return score

def main():
	start_time = time.time()
	names = []
	file = "22.txt"
	in_file = open(file, "r")
	for line in in_file:
		line = line.strip()
		line = line.split("\",\"")
		names = line
	names[0] = 'MARY'
	names[-1] = 'ALONSO'

	insertionSort(names)
	
	# Calculate score
	total_score = 0
	for i in range(len(names)):
		total_score += getScore(names[i])*(i+1)

	print("The total of all the name scores in the file is: " + str(total_score))

	elapsed_time = time.time() - start_time
	print("\nTime elapsed: " + str(elapsed_time))

main()  
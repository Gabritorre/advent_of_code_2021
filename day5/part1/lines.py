
matrix = [[0 for i in range(999)] for i in range(999)]
arrxy1 = []		#value in the left of "->"
arrxy2 = []		#value in the right of "->"
input = open("input.txt", "r")
for line in input.readlines():
	tempArray = line.split(" -> ")

	tmp = tempArray[0].split(",")
	arrxy1.append(int(tmp[0]))
	arrxy1.append(int(tmp[1]))

	tmp = tempArray[1].split(",")
	arrxy2.append(int(tmp[0]))
	arrxy2.append(int(tmp[1].strip("\n")))

# when the index is i we are referring to x, when the index is i+1 we are referring to y
for i in range(0, len(arrxy1), 2):
	if(arrxy1[i] == arrxy2[i]):		#x1 = x2
		if(arrxy1[i+1] < arrxy2[i+1]):	#y1 < y2
			for j in range(arrxy1[i+1], arrxy2[i+1] + 1):	#fill from y1 to y2
				matrix[arrxy1[i]][j] += 1
		elif(arrxy1[i+1] > arrxy2[i+1]):	#y1 > y2
			for j in range(arrxy2[i+1], arrxy1[i+1] + 1):	#fill from y2 to y1
				matrix[arrxy1[i]][j] += 1

	elif(arrxy1[i+1] == arrxy2[i+1]):	#y1 = y2
		if(arrxy1[i] < arrxy2[i]):	#x1 < x2
			for j in range(arrxy1[i], arrxy2[i] + 1):	#fill from x1 to x2
				matrix[j][arrxy1[i+1]] += 1
		elif(arrxy1[i] > arrxy2[i]):	#x1 > x2
			for j in range(arrxy2[i], arrxy1[i] + 1):	#fill from x2 to x1
				matrix[j][arrxy1[i+1]] += 1

result = 0
for i in range(0, len(matrix)):
	for j in range(0, len(matrix)):
		if(matrix[i][j] >= 2):
			result += 1
print("result: ", result)

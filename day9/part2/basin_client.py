import socket
COLUMNS = 100

def fillMatrix(line, row):
	for i in range(COLUMNS):
		matrix[row][i] = int(line[i])

def findBasin(row, column):
	global counter
	value = matrix[row][column]
	matrix[row][column] = 9
	try:
		if(matrix[row-1][column] >= value and matrix[row-1][column] != 9 and row != 0):
			counter += 1
			findBasin(row-1, column)
	except IndexError:
		print(end = "")
	try:
		if(matrix[row][column+1] >= value and matrix[row][column+1] != 9):
			counter += 1
			findBasin(row, column+1)
	except IndexError:
		print(end = "")
	try:
		if(matrix[row+1][column] >= value and matrix[row+1][column] != 9):
			counter += 1
			findBasin(row+1, column)
	except IndexError:
		print(end = "")
	try:
		if(matrix[row][column-1] >= value and matrix[row][column-1] != 9 and column != 0):
			counter += 1
			findBasin(row, column-1)
	except IndexError:
		print(end = "")

def checkBasin():
	if(counter > result[result.index(min(result))]):	#if counter is greater than le smallest in the result list
		result[result.index(min(result))] = counter

s = socket.socket()
s.connect(("localhost", 1111))

length = int(s.recv(1024).decode())
matrix = [[0 for i in range(COLUMNS)] for i in range(length)]
line = ""
for i in range(length):
	line = s.recv(COLUMNS + 2).decode()	#COLUMNS + 2 because of the new line ("\n")
	fillMatrix(line, i)
	s.send("ok".encode())

result = []
for i in range(3):
	result.append(1)

counter = 1

for i in range(1, length-1):
	for j in range(1, COLUMNS-1):
		if(matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i][j+1] and matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j-1]):
			findBasin(i, j)
			checkBasin()
			counter = 1


#border of the matrix
for i in range(0, length, length-1):
	for j in range(0, COLUMNS):
		if(i == 0):
			if(j == 0):
				if(matrix[i][j] < matrix[i][j+1] and matrix[i+1][j]):
					findBasin(i, j)
					checkBasin()
					counter = 1
			elif(j == COLUMNS-1):
				if(matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j-1]):
					findBasin(i, j)
					checkBasin()
					counter = 1
			else:
				if(matrix[i][j] < matrix[i][j+1] and matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j-1]):
					findBasin(i, j)
					checkBasin()
					counter = 1
		else:
			if(j == 0):
				if(matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i][j+1]):
					findBasin(i, j)
					checkBasin()
					counter = 1
			elif(j == COLUMNS-1):
				if (matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i][j-1]):
					findBasin(i, j)
					checkBasin()
					counter = 1
			else:
				if(matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i][j+1] and matrix[i][j] < matrix[i][j-1]):
					findBasin(i, j)
					checkBasin()
					counter = 1

for j in range(0, COLUMNS, COLUMNS-1):
	for i in range(1, length-1):
		if(j == 0):
			if(matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i][j+1] and matrix[i][j] < matrix[i+1][j]):
				findBasin(i, j)
				checkBasin()
				counter = 1
		else:
			if(matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j-1]):
				findBasin(i, j)
				checkBasin()
				counter = 1


final = 1
for i in range(len(result)):
	final *= result[i]

print(final)

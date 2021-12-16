import socket
COLUMNS = 100
def fillMatrix(line, row):
	for i in range(COLUMNS):
		matrix[row][i] = int(line[i])
	
s = socket.socket()
s.connect(("localhost", 1111))

length = int(s.recv(1024).decode())
matrix = [[0 for i in range(COLUMNS)] for i in range(length)]
line = ""
for i in range(length):
	line = s.recv(COLUMNS + 2).decode()	#COLUMNS + 2 because of the new line ("\n")z
	fillMatrix(line, i)
	s.send("ok".encode())


result = 0
for i in range(1, length-1):
	for j in range(1, COLUMNS-1):
		if(matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i][j+1] and matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j-1]):
			result += matrix[i][j] + 1

#border of the matrix
for i in range(0, length, length-1):
	for j in range(0, COLUMNS):
		if(i == 0):
			if(j == 0):
				if(matrix[i][j] < matrix[i][j+1] and matrix[i+1][j]):
					result += matrix[i][j] + 1
			elif(j == COLUMNS-1):
				if(matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j-1]):
					result += matrix[i][j] + 1
			else:
				if(matrix[i][j] < matrix[i][j+1] and matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j-1]):
					result += matrix[i][j] + 1
		else:
			if(j == 0):
				if(matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i][j+1]):
					result += matrix[i][j] + 1
			elif(j == COLUMNS-1):
				if (matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i][j-1]):
					result += matrix[i][j] + 1
			else:
				if(matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i][j+1] and matrix[i][j] < matrix[i][j-1]):
					result += matrix[i][j] + 1

for j in range(0, COLUMNS, COLUMNS-1):
	for i in range(1, length-1):
		if(j == 0):
			if(matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i][j+1] and matrix[i][j] < matrix[i+1][j]):
				result += matrix[i][j] + 1
		else:
			if(matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j-1]):
				result += matrix[i][j] + 1

print(result)


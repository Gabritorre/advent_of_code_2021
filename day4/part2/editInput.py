inputfile = open("rawinput.txt", 'r')
outputfile = open("modinput.txt", 'a')

first_line = inputfile.readline()
first_line = first_line.rstrip("\n")
outputfile.write("<h1>")
outputfile.write(first_line)
outputfile.write("</h1>\n")

for line in inputfile.readlines():
	if(line != "\n"):
		outputfile.write("<p>")
		line = line.rstrip("\n")
		outputfile.write(line)
		outputfile.write("</p>\n")

inputfile.close()
outputfile.close()
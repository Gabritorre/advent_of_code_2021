package main
// each unknown number (or string that rappresent an unknown number 0, 2, 3, 5, 6, 9) have a known number (1, 4, 7, 8) that can decode it
// for example the string that rappresent number 9 can be decoded with number 4: if we remove the letters present in 4's string in the 9's string, only 2 letters remains in the string
// this not happens with numbers 0 and 6 (that have the same lenght of 9's string), so we have recognized 9.
import (
	"fmt"
	"os"
	"bufio"
	"strings"
	"strconv"
	)


func main() {
	file, err:= os.Open("input.txt")
	if err != nil {
		fmt.Printf("hello")
	}
	var lines [800]string	//this contains the string in the left side of "|"
	var pattern [800]string	//this contains only the numbers 1, 4, 7, 8 in the left side of "|"
	index := 0
	indexP := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		tempLine := scanner.Text()
		temp := strings.Split(tempLine, " | ")

		tempDigit := strings.Split(temp[1], " ")
		for i := 0; i < len(tempDigit); i++ {
			lines[index] = tempDigit[i]
			index++
		}
		tempPattern := strings.Split(temp[0], " ")
		
		for i := 0; i < len(tempPattern); i++{
			if len(tempPattern[i]) == 2 || len(tempPattern[i]) == 4 || len(tempPattern[i]) == 3 || len(tempPattern[i]) == 7 {
				pattern[indexP] = tempPattern[i]
				indexP++
			}
			
		}
	}
	result := 0
	value := ""
	index = 0
	var key1 string
	var key2 string
	var checkString string
	for i := 0; i < len(lines); i+=4 {
		for j := 0; j < 4; j++ {
			if len(lines[index]) == 2{
				value = value + "1"
			} else if len(lines[index]) == 3{
				value = value + "7"
			} else if len(lines[index]) == 4{
				value = value + "4"
			} else if len(lines[index]) == 7{
				value = value +  "8"
			} else if len(lines[index]) == 5{	// can be 5, 2, 3
				for h := i; h < (i+4); h++{	
					if len(pattern[h]) == 4{	//search for string that rappresent number 4
						key1 = pattern[h]
					}
					if len(pattern[h]) == 3{	//search for string that rappresent number 7
						key2 = pattern[h]
					}
				}
				checkString = lines[index]
				for h := 0; h < len(key2); h++{
					checkString = strings.Replace(checkString, string(key2[h]), "", 1)
				}
				if len(checkString) == 2{
					value = value + "3"
				} else{
					checkString = lines[index]
					for h := 0; h < len(key1); h++{
						checkString = strings.Replace(checkString, string(key1[h]), "", 1)
					}
					if len(checkString) == 2{
						value = value + "5"
					}else{
						value = value + "2"
					}
					
				}
			} else if len(lines[index]) == 6{ 	// can be 9, 6, 0
				for h := i; h < (i+4); h++{	
					if len(pattern[h]) == 4{	//search for string that rappresent number 4
						key1 = pattern[h]
					}
					if len(pattern[h]) == 2{	//search for string that rappresent number 1
						key2 = pattern[h]
					}
				}
				checkString = lines[index]
				for h := 0; h < len(key2); h++{
					checkString = strings.Replace(checkString, string(key2[h]), "", 1)
				}
				if len(checkString) == 5{
					value = value + "6"
				} else{
					checkString = lines[index]
					for h := 0; h < len(key1); h++{
						checkString = strings.Replace(checkString, string(key1[h]), "", 1)
					}
					if len(checkString) == 2{
						value = value + "9"
					}else{
						value = value + "0"
					}
				}
			}
			index++
		}
		temp, err := strconv.Atoi(value)
		if err != nil {
			fmt.Println(err)
			os.Exit(2)
		}
		result += temp
		value = ""
	}
	fmt.Println("result: ", result)
}
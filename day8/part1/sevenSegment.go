package main

import (
	"fmt"
	"os"
	"bufio"
	"strings"
	)

func main() {
	file, err:= os.Open("input.txt")
	if err != nil {
		fmt.Printf("hello")
	}
	var lines [800]string
	index := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		tempLine := scanner.Text()
		temp := strings.Split(tempLine, " | ")
		temp = strings.Split(temp[1], " ")
		for i := 0; i < len(temp); i++ {
			lines[index] = temp[i]
			index++
		}	
	}
	counter := 0
	for i := 0; i < len(lines); i++ {
		if(len(lines[i]) == 2 || len(lines[i]) == 3 || len(lines[i]) == 4 || len(lines[i]) == 7){
			counter++
		}
	}
	
	fmt.Println(counter)
}

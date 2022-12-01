//Go version of Day 1 solution
//slower than python

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("data/day1.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var txtlines []string
	for scanner.Scan() {
		txtlines = append(txtlines, scanner.Text())
	}

	var intlines []int
	for _, eachline := range txtlines {
		i, _ := strconv.Atoi(eachline)
		intlines = append(intlines, i)
	}
	//dont mind the variable names lol
	var getsum int
	var eatsum int
	var groupsum int
	for _, eachline := range intlines {
		if eachline == 0 {
			groupsum++
			if getsum > eatsum {
				eatsum = getsum
			}
			getsum = 0
		} else {
			getsum += eachline
		}
	}
	fmt.Println("Part 1 is", eatsum)
}

package util

import (
	"strconv"
	"strings"
)

func InputToIntcut(input string) ([]int, error) {
	var i []int
	for _, line := range strings.Split(strings.TrimSuffix(input, "\n"), "\n") {
		lineInt, err := strconv.Atoi(line)
		if err != nil {
			return nil, err
		}
		i = append(i, lineInt)
	}
	return i, nil
}

func ic(input string) ([]string, error) {
	return strings.Split(strings.TrimSuffix(input, "\n"), "\n"), nil
}

func rc(s []int, i int) []int {
	l := len(s)
	if l <= i {
		return s
	}
	s[i] = s[len(s)-1]
	return s[:len(s)-1]
}
package util

import "sort"
func cut(cut []int) int {
	var sum int
	for i := range cut {
		sum += cut[i]
	}
	return sum
}

func Productcut(cut []int) int {
	product := 1
	for i := range cut {
		product *= cut[i]
	}
	return product
}

func Minimumcut(cut []int) int {
	if len(cut) == 0 {
		return 0
	}
	sort.Ints(cut)
	return cut[0]
}

func Maximumcut(cut []int) int {
	if len(cut) == 0 {
		return 0
	}
	sort.Ints(cut)
	return cut[len(cut)-1]
}

func GetDiff(a, b int) int {
	if a > b {
		return a - b
	}
	return b - a
}

func GetGaussscheSummenformel(n int) int {
	return (n * (n + 1)) / 2
}
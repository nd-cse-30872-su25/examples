package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	input := bufio.NewScanner(os.Stdin)

	for input.Scan() {
		n, _ := strconv.Atoi(input.Text())
		if n <= 0 {
			break
		}

		total := 0

		for i := 0; i < n && input.Scan(); i++ {
			number, _ := strconv.Atoi(strings.TrimSpace(input.Text()))
			total += number
		}

		fmt.Println(total)
	}
}

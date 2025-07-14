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
		numbers := strings.Fields(input.Text())
		total := 0
		for _, number := range numbers {
			n, _ := strconv.Atoi(number)
			total += n
		}

		fmt.Println(total)
	}
}

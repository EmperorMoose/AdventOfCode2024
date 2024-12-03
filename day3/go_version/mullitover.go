package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	text, err := readFile()
	if err != nil {
		fmt.Println("error:", err)
	}

	muls := getValidMuls(text)
	sum := sumPairs(muls)
	fmt.Println("Read Content:")
	fmt.Println(sum)
}

func sumPairs(commands [][2]string) int {
	var products []int

	for _, pair := range commands {
		x, err1 := strconv.Atoi(pair[0])
		y, err2 := strconv.Atoi(pair[1])

		if err1 == nil && err2 == nil {
			products = append(products, x*y)
		}
	}

	total := 0
	for _, product := range products {
		total += product
	}

	return total
}

func getValidMuls(text string) [][2]string {
	mulsRegex := regexp.MustCompile(`mul\((\d+),(\d+)\)`)
	ctrlRegex := regexp.MustCompile(`do\(\)|don't\(\)`)

	var commands [][2]string
	readCtrl := true
	splitText := ctrlRegex.Split(text, -1)
	ctrlMatches := ctrlRegex.FindAllString(text, -1)

	for i, segment := range splitText {

		if i < len(ctrlMatches) {
			if ctrlMatches[i] == "do()" {
				readCtrl = true
			} else if ctrlMatches[i] == "don't()" {
				readCtrl = false
			}
		}

		if readCtrl {
			matches := mulsRegex.FindAllStringSubmatch(segment, -1)
			for _, match := range matches {
				commands = append(commands, [2]string{match[1], match[2]})
			}
		}
	}

	return commands
}

func readFile() (string, error) {
	file, err := os.Open("input.txt")
	if err != nil {
		return "", fmt.Errorf("failed to open file", err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)
	var contentBuilder strings.Builder

	for scanner.Scan() {
		line := scanner.Text()
		contentBuilder.WriteString(line)
		contentBuilder.WriteString("\n")
	}

	if err := scanner.Err(); err != nil {
		return "", fmt.Errorf("failed to open file", err)
	}

	content := contentBuilder.String()
	return content, nil
}

#!/usr/bin/python

# https://adventofcode.com/2022/day/3

from string import ascii_letters


def rucksack_input():
	rucksacks = list()
	print("The Rucksack contents:\nPlease enter empty line to finish input")
	while True:
		line = input()
		if line:
			line = line.strip()
			rucksacks.append((line[:len(line)//2], line[len(line)//2:]))
		else:
			break
	return rucksacks


def item_priority(item):
	return ascii_letters.index(item) + 1
	

if __name__ == "__main__":
	rucksacks = rucksack_input()
	priority_sum = 0
	for num, rucksack in enumerate(rucksacks, 1):
		for item in rucksack[0]:
			if item in rucksack[1]:
				priority_sum += item_priority(item)
				break
	print(priority_sum)


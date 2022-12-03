#!/usr/bin/python

# https://adventofcode.com/2022/day/3

from string import ascii_letters


def rucksack_input(group=False):
	rucksacks = list()
	variable = "Group" if group else "Rucksack"
	print("The {variable} contents:\nPlease enter empty line to finish input\n")
	group_index = 0
	while True:
		line = input()
		if line:
			line = line.strip()
			if group:
				if group_index % 3 == 0:
					rucksacks.append(list())
				rucksacks[-1].append(
					(line[:len(line)//2], line[len(line)//2:]))
			else:
				rucksacks.append(
					(line[:len(line)//2], line[len(line)//2:]))
		else:
			break
		group_index += 1
	return rucksacks


def item_priority(item):
	return ascii_letters.index(item) + 1


def sum_of_rucksack_priorities(rucksacks):
	priority_sum = 0
	for num, rucksack in enumerate(rucksacks, 1):
		for item in rucksack[0]:
			if item in rucksack[1]:
				priority_sum += item_priority(item)
				break
	return priority_sum


def sum_of_group_priorities(groups):
	priority_sum = 0
	for num, group in enumerate(groups, 1):
		for item in str.join(*group[0]):
			if item in str.join(*group[1]) and item in str.join(*group[2]):
				priority_sum += item_priority(item)
				break
	return priority_sum


if __name__ == "__main__":
	if input("Rucksack or Group priority summing? r/g") == "r":
		rucksacks = rucksack_input(group=False)
		print(sum_of_rucksack_priorities(rucksacks))
	else:
		rucksacks = rucksack_input(group=True)
		print(sum_of_group_priorities(rucksacks))


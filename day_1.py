#!/usr/bin/python

# https://adventofcode.com/2022/day/1

def inventory_input():
	inventories, index = [list()], 0
	print("The Elves Invetory:\nPlease enter 'end' to finish input")
	while True:
		line = input()
		if line.isnumeric():
			inventories[index].append(int(line))
		elif "end" in line:
			break
		else:
			index += 1
			inventories.append(list())
	return list(filter(None, inventories))


if __name__ == "__main__":
	elf_inventories = inventory_input()
	elf_inventories = [sum(inventory) for inventory in elf_inventories]
	index_of_elf = elf_inventories.index(list(sorted(elf_inventories))[-1])
	print(index_of_elf+1, elf_inventories[index_of_elf])

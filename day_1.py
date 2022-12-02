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
	elf_inventories.sort()
	print(f"Answer to Part 1: {elf_inventories[-1]}")
	print(f"Answer to Part 2: {sum(elf_inventories[-3:])}")

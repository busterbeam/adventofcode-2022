#!/usr/bin/python

# https://adventofcode.com/2022/day/2

from pprint import pprint

def strategy_guide_input():
	strategies = list()
	print("The Strategy guide:\nPlease enter empty line to finish input")
	while True:
		line = input()
		if line:
			strategies.append(line.split(' '))
		else:
			break
	return list(filter(None, strategies))

scoring = {	
	"X": 1, "A": 1, # Rock
	"Y": 2, "B": 2, # Paper
	"Z": 3, "C": 3, # Scissors
}


if __name__ == "__main__":
	strategies = strategy_guide_input()
	score = 0
	for strategy in strategies:
		opponent, you = strategy
		if opponent == "A":
			score += 3 if you == "X" else (6 if you == "Y" else 0)
		elif opponent == "B":
			score += 0 if you == "X" else (3 if you == "Y" else 6)
		else:
			score += 6 if you == "X" else (0 if you == "Y" else 3)
		score += scoring[you]
	print(score)

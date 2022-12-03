#!/usr/bin/python

# https://adventofcode.com/2022/day/2

def strategy_guide_input():
	strategies = list()
	print("The Strategy guide:\nPlease enter empty line to finish input")
	while True:
		line = input()
		if line:
			strategies.append(line.strip().split(' '))
		else:
			break
	return list(filter(None, strategies))


METRIC = {	
	"X": 1, "A": 1, # Rock
	"Y": 2, "B": 2, # Paper
	"Z": 3, "C": 3, # Scissors
}


def win_or_lose(opponent, you):
	if opponent == "A":
		return 3 if you == "X" else (6 if you == "Y" else 0)
	elif opponent == "B":
		return 0 if you == "X" else (3 if you == "Y" else 6)
	else:
		return 6 if you == "X" else (0 if you == "Y" else 3)


if __name__ == "__main__":
	strategies = strategy_guide_input()
	score = 0
	for strategy in strategies:
		opponent, you = strategy
		result = 0 if you == "X" else (3 if you == "Y" else 6)
		for move in ["X", "Y", "Z"]:
			if result == win_or_lose(opponent, move):
				you = move
				break
		score += METRIC[you] + result
		
	print(score)


#!/usr/bin/env python3

import argparse
import random
import sys

# The main function of the program, responsible for doing all the processing with files
def main(args):

	# Get all the lines for randomizing the output
	lines = []

	for f in args.files:
		for line in f:
			lines.append(line)

	# Randomize if needed
	if args.randomize:
		random.shuffle(lines)

	# Use a temporary variable for keeping track in where to put the group delimiter
	i = 1

	# Print everything to the output as delimited
	for line in lines:
		# Print the line to output
		print(line, file=args.output, end="")

		# If group is full, print delimiter
		if i == args.size:
			print(args.delimiter, file=args.output)
			i = 1
		else:
			i += 1

	# Program end

# Parse command line arguments
def parse_args():
	parser = argparse.ArgumentParser(description='Group given input file(s) with given group size and delimiter')

	pa = parser.add_argument

	pa('-s', '--size', type=int, help='set group size, default is 3', default=3)
	pa('-d', '--delimiter', type=str, help='group delimiter, default is empty string', default='')
	pa('-r', '--randomize', action='store_true', help='randomize entries before grouping them')
	pa('-o', '--output', type=str, help='set output file, default is standard output', default=sys.stdout)
	pa('files', nargs='*', type=argparse.FileType('r'), help='input file, default is standard input', default=sys.stdin)

	args = parser.parse_args()

	if type(args.files) != list:
		args.files = [args.files]

	return args

if __name__ == '__main__':
	main(parse_args())

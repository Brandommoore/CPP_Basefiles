# Cpp generator from Hpp file header

import argparse
from ast import arg
from io import open
import os

class File_data():
	filename = ""
	class_name = ""
	methods = []

#################################
##	Program parser
#################################

def	clean_file_lines(file_lines):
	'''Clean line break lines and return a clean list of lines'''
	clean_lines = []
	for line in file_lines:
		if line != "\n" and line != "\0":
			clean_lines.append(line)
	return clean_lines

def	read_file(filename):
	'''Read file and return a list with the file lines'''
	file = open(filename, "r");
	file_lines = file.readlines()
	file.close()
	return clean_file_lines(file_lines)

def	program_parser():
	'''Parse the program input. hpp_file is required'''
	parser = argparse.ArgumentParser(
		formatter_class=argparse.RawDescriptionHelpFormatter,
		description="Cpp generator from Hpp file header "
	);
	parser.add_argument("hpp_file", help="HPP file header")
	args = parser.parse_args()
	return args

#################################
##	File parser
#################################

def	get_class_name(file_lines):
	'''Gat class name and return it name'''
	class_name = ""
	for line in file_lines:
		if "class" in line:
			split_line = line.split()
			return split_line[-1]

def	file_parser(file_data):
	'''Fond class and methods and save it in file_data'''
	file_lines = read_file(file_data.filename);
	for line in file_lines:
		print(line, end='')
	print(f"Class name --> {get_class_name(file_lines)}")

if __name__ == '__main__':
	file_data = File_data()
	p_parser = program_parser()
	file_data.filename = p_parser.hpp_file
	print(f"Cpp generator from {file_data.filename}")
	file_parser(file_data)



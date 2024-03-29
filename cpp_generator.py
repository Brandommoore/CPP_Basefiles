# Cpp generator from Hpp file header

import argparse
from ast import arg
from io import open
import os

#################################
##	Main Class
#################################

class File_data():
	filename = ""
	class_name = ""
	file_lines = []
	in_methods = []
	out_methods = []


#################################
##	Utils
#################################

def	write_header(file, c_type):
	'''Write header into a file
	   file: File for write
	   c_type: [m] --> Makefile
		   [x] --> Cpp & Hpp
	'''
	if c_type == 'm':
		init_c = '#'
		end_c = '#'
	if c_type == 'x':
		init_c = '/*'
		end_c = '*/'

	header=[]
	header.append(init_c + " **************************************************************************** " + end_c)
	header.append(init_c + "                                                                              " + end_c)
	header.append(init_c + "                                                         :::      ::::::::    " + end_c)
	header.append(init_c + "    cpp_from_hpp_gen.py                                :+:      :+:    :+:    " + end_c)
	header.append(init_c + "                                                     +:+ +:+         +:+      " + end_c)
	header.append(init_c + "    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         " + end_c)
	header.append(init_c + "                                                 +#+#+#+#+#+   +#+            " + end_c)
	header.append(init_c + "    Created: 2022/10/18 18:56:07 by marvin            #+#    #+#              " + end_c)
	header.append(init_c + "    Updated: 2022/10/18 18:56:07 by marvin           ###   ########.fr        " + end_c)
	header.append(init_c + "                                                                              " + end_c)
	header.append(init_c + " **************************************************************************** " + end_c)
	
	for component in header:
		file.write(component)
		file.write("\n")
	file.write("\n")

def	filename_checker(filename: str, file_ext: str):
	'''Checks if the file extension is correct'''
	split_name = filename.split('.')
	if split_name[-1] == file_ext:
		return 1
	else:
		return 0

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
	'''Get class name and return it name'''
	for line in file_lines:
		if "class" in line:
			split_line = line.split()
			return split_line[-1]

def	find_methods(file_data):
	'''Find methods and allocate in file_data'''
	f_data = file_data
	bracket = 0
	for line in f_data.file_lines:
		if "{" in line or "}" in line:
			bracket+=1
		if ("(" in line and ")" in line) and bracket < 2:
			f_data.in_methods.append(del_spaces_before_text(line))
		if ("(" in line and ")" in line) and bracket >= 2:
			f_data.out_methods.append(del_spaces_before_text(line))
	return f_data

def del_spaces_before_text(input_string):
	'''Return a string without spaces before the text'''
	index = 0
	while index < len(input_string) and input_string[index].isspace():
		index += 1
	modified_string = input_string[index:]
	return modified_string

def	print_values(values: list):
	'''Print list of values'''
	for val in values:
		print(val, end='')

def	file_parser(file_data):
	'''Find class and methods and save it in file_data'''
	file_data.file_lines = read_file(file_data.filename);
	file_data.class_name = get_class_name(file_data.file_lines);
	file_data = find_methods(file_data)
	return file_data

#################################
##	CPP FILE Generator
#################################

def	format_method(class_name: str, method: str):
	'''Format method adding the name_class to method and return it
	   TYPE: [IN] [OUT] (method)
	   CLASS_NAME: name of the class
	   METHOD: method to format
	'''
	final_method = []
	nb_tabs = 0
	i = 0

	split_method = method.split()
	nb_tabs = count_tabs(method)
	if class_name in split_method[0]:
		final_method.append(class_name + "::")
		for word in split_method:
			final_method.append(word)
	elif class_name is not split_method[0]:
		final_method.append(split_method[0])
		final_method.append(print_tabs(nb_tabs))
		final_method.append(class_name + "::")
		for word in split_method:
			if i == 0:
				i+=1
			elif i >= 1:
				final_method.append(word)
	final_method.append("\n")
	return remove_semicolon("".join(final_method))


def	format_all_methods(type_m, methods_list: list, class_name):
	'''Iterate formats and call format_method every method
		   TYPE: [IN] [OUT] (method)'''
	final_methods = []
	if type_m == "IN":
		for method in methods_list:
			final_methods.append(format_method(class_name, method))
	elif type_m == "OUT":
		for method in methods_list:
			final_methods.append(remove_semicolon(method))
	return final_methods

def count_tabs(string):
	'''Count the nuber of tabs in a string'''
	tab_count = 0
	for char in string:
		if char == '\t':
			tab_count += 1
	return tab_count

def print_tabs(nb_tabs: int):
	'''Return a string with nb tabs'''
	string_tab = []
	for i in range(nb_tabs):
		string_tab.append("\t")
	return "".join(string_tab)

def	remove_semicolon(string):
	'''Remove semicolon of a string'''
	result = ""
	for char in string:
		if char != ';':
			result += char
	return result



def	write_cpp_file(file_data):
	'''Write the cpp file'''
	filename = file_data.class_name + ".cpp"
	file = open(filename, "w")
	write_header(file, "x")
	file.write('#include "' + file_data.class_name + '.hpp"\n\n')
	for method in file_data.in_methods:
		file.write(method)
		file.write("{\n\n}\n\n")
	if file_data.out_methods != None and len(file_data.out_methods) > 0:
		file.write("\n// Other functions in " + file_data.filename + " outer class "
		+ file_data.class_name + "\n\n")
		for method in file_data.out_methods:
			file.write(method)
			file.write("{\n\n}\n\n")
	file.close()


def	file_generator(file_data):
	'''Generate the main content of the CPP file'''
	main_content = []
	file_data.in_methods = format_all_methods("IN", file_data.in_methods, file_data.class_name)
	file_data.out_methods = format_all_methods("OUT", file_data.out_methods, file_data.class_name)
	write_cpp_file(file_data)


#################################
##	Main
#################################

if __name__ == '__main__':
	file_data = File_data()
	p_parser = program_parser()
	if filename_checker(p_parser.hpp_file, "hpp") == 1:
		file_data.filename = p_parser.hpp_file
		print(f"Cpp generator from {file_data.filename}")
		file_data = file_parser(file_data)
		file_generator(file_data)
		print("\n\t" + file_data.class_name + ".cpp generated from " + file_data.filename + " --> DONE <--")
	else:
		print("Please, insert a File.hpp file")




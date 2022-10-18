# Base files for CPP generator

import argparse
from ast import arg
from io import open
import os

def	print_header(file, c_type):
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
	header.append(init_c + "    basefiles_gen.py                                   :+:      :+:    :+:    " + end_c)
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
	

def	makefile_gen(project_name):
	mk_comps=[]
	mk_name = 'NAME = ' + project_name
	mk_src = 'SRC = ' + project_name + ".cpp"
	mk_head = 'HEAD = ' + project_name + ".hpp"
	mk_comps.append(str(mk_name))
	mk_comps.append(str(mk_src))
	mk_comps.append(str(mk_head))
	mk_comps.append('OBJ = $(SRC:%.cpp=%.o)')
	mk_comps.append('CXX = clang++ -std=c++98 -pedantic')
	mk_comps.append('CXXFLAGS = -Wall -Werror -Wextra')
	mk_comps.append('CFNAME = -o $(NAME)')
	mk_comps.append('all: $(NAME)')
	mk_comps.append('$(NAME): $(OBJ) $(HEAD)\n\t$(CXX) $(CXXFLAGS) $(OBJ) $(CFNAME)')
	mk_comps.append('clean:\n\trm -rf $(OBJ)')
	mk_comps.append('fclean: clean\n\trm -rf $(OBJ) $(NAME)')
	mk_comps.append('re: fclean all')
	mk_comps.append('.PHONY: all clean fclean re')

	file = open("Makefile", 'w')
	print_header(file, 'm')

	for component in mk_comps:
		file.write(component)
		file.write("\n\n")
	file.close()
	print("\tMakefile done")


def	hpp_generator(project_name):
	hpp_comps=[]
	header_name = project_name.upper() + "_H"
	hpp_comps.append(str("#ifndef " + header_name + "\n"))
	hpp_comps.append(str("# define " + header_name + "\n"))
	hpp_comps.append("\n")
	hpp_comps.append("#include <iostream>\n")
	hpp_comps.append("\n#endif\n")

	filename = str(project_name + ".hpp")
	file = open(filename, 'w')
	print_header(file, 'x')
	for component in hpp_comps:
		file.write(component)
	file.close()
	print("\tHpp file done")


def	cpp_generator(project_name):
	cpp_comps=[]
	include_name = '#include "' + project_name + '.hpp"\n\n'
	cpp_comps.append("int\tmain(int argc, char *argv[])\n")
	cpp_comps.append("{\n\n")
	cpp_comps.append("}\n")

	filename = str(project_name + ".cpp")
	file = open(filename, 'w')
	print_header(file, 'x')
	file.write(include_name)
	for component in cpp_comps:
		file.write(component)
	file.close()
	print("\tCpp file done")


if __name__ == '__main__':
	parser = argparse.ArgumentParser();
	parser.add_argument("p_name", help="Project name. USAGE: [basefiles_gen.py project_name]");
	args = parser.parse_args()
	print('Base files for cpp generator:\n')
	makefile_gen(args.p_name)
	hpp_generator(args.p_name)
	cpp_generator(args.p_name)
	print("\nAll done")

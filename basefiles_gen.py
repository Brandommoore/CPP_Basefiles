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
	mk_src = "SRC =\tmain.cpp \\\n\t\t" + project_name + ".cpp"
	mk_head = 'HEAD = ' + project_name + ".hpp"
	mk_comps.append(str(mk_name))
	mk_comps.append(str(mk_src))
	mk_comps.append('OBJ = $(SRC:%.cpp=%.o)')
	mk_comps.append('CXX = clang++')
	mk_comps.append('CXXFLAGS = -Wall -Werror -Wextra -std=c++98 -pedantic')
	mk_comps.append('all: $(NAME)')
	mk_comps.append('$(NAME): $(OBJ)\n\t$(CXX) $(CXXFLAGS) $(OBJ) -o $(NAME)')
	mk_comps.append('clean:\n\trm -rf $(OBJ)')
	mk_comps.append('fclean: clean\n\trm -rf $(NAME)')
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
	header_name = project_name.upper() + "_H__"
	hpp_comps.append(str("#ifndef __" + header_name + "\n"))
	hpp_comps.append(str("# define __" + header_name + "\n"))
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

	filename = str(project_name + ".cpp")
	file = open(filename, 'w')
	print_header(file, 'x')
	file.write(include_name)
	for component in cpp_comps:
		file.write(component)
	file.close()
	print("\tCpp file done")

def	main_generator(project_name):
	cpp_comps=[]
	include_name = '#include "' + project_name + '.hpp"\n\n'
	cpp_comps.append("int\tmain(int argc, char *argv[])\n")
	cpp_comps.append("{\n\n")
	cpp_comps.append("\t(void)argc;\n\t(void)argv;\n\treturn (0);\n")
	cpp_comps.append("}\n")

	file = open("main.cpp", 'w')
	print_header(file, 'x')
	file.write(include_name)
	for component in cpp_comps:
		file.write(component)
	file.close()
	print("\tMain file done")

def generator(args):
	if args.M is True:
		makefile_gen(args.p_name)
	if args.H is True:
		hpp_generator(args.p_name)
	if args.C is True:
		cpp_generator(args.p_name)
	if args.M is False and args.H is False and args.C is False:
		makefile_gen(args.p_name)
		hpp_generator(args.p_name)
		cpp_generator(args.p_name)
		main_generator(args.p_name)


def parser():
	parser = argparse.ArgumentParser(
		formatter_class=argparse.RawDescriptionHelpFormatter,
		description="A basefiles generator for cpp modules ",
		epilog="==================================================\n\
This is a generator of basefiles for cpp modules. By default it generates a Makefile, a .cpp and a .hpp ready to compile.\n\
If, for example, we only want to generate a Makefile, we would do it as follows, and so on with the rest:\n\
	basefiles_gen.py project_name -M\n\n\
If we want to generate only the .cpp and .hpp files:\n\
	basefiles_gen.py project_name -C -H\n\n\
By mcordoba (@brandommoore) with ❤"
	);
	parser.add_argument("p_name", help="Project name. USAGE: [basefiles_gen.py project_name]");
	parser.add_argument("-M", "-makefile", action='store_true', help="Only generates Makefile")
	parser.add_argument("-C", "-cpp", action='store_true', help="Only generates Cpp")
	parser.add_argument("-H", "-hpp", action='store_true', help="Only generates Hpp")

	args = parser.parse_args()
	return args


if __name__ == '__main__':
	args = parser()
	print('Base files for cpp generator:\n')
	generator(args)
	print("\nAll done")

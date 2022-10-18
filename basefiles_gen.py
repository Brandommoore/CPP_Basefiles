# Base files for CPP generator

import argparse
from io import open
import os

def	print_makefile_header(file):
	header=[]
	header.append('#' + " **************************************************************************** " + "#")
	header.append('#' + "                                                                              " + "#")
	header.append('#' + "                                                         :::      ::::::::    " + "#")
	header.append('#' + "    basefiles_gen.py                                   :+:      :+:    :+:    " + "#")
	header.append('#' + "                                                     +:+ +:+         +:+      " + "#")
	header.append('#' + "    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         " + "#")
	header.append('#' + "                                                 +#+#+#+#+#+   +#+            " + "#")
	header.append('#' + "    Created: 2022/10/18 18:56:07 by marvin            #+#    #+#              " + "#")
	header.append('#' + "    Updated: 2022/10/18 18:56:07 by marvin           ###   ########.fr        " + "#")
	header.append('#' + "                                                                              " + "#")
	header.append('#' + " **************************************************************************** " + "#")
	
	for component in header:
		file.write(component)
		file.write("\n")
	file.write("\n")

def	print_cpp_hpp_header(file):
	header=[]
	header.append('/*' + " **************************************************************************** " + "*/")
	header.append('/*' + "                                                                              " + "*/")
	header.append('/*' + "                                                         :::      ::::::::    " + "*/")
	header.append('/*' + "    basefiles_gen.py                                   :+:      :+:    :+:    " + "*/")
	header.append('/*' + "                                                     +:+ +:+         +:+      " + "*/")
	header.append('/*' + "    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         " + "*/")
	header.append('/*' + "                                                 +#+#+#+#+#+   +#+            " + "*/")
	header.append('/*' + "    Created: 2022/10/18 18:56:07 by marvin            #+#    #+#              " + "*/")
	header.append('/*' + "    Updated: 2022/10/18 18:56:07 by marvin           ###   ########.fr        " + "*/")
	header.append('/*' + "                                                                              " + "*/")
	header.append('/*' + " **************************************************************************** " + "*/")
	
	for component in header:
		file.write(component)
		file.write("\n")
	file.write("\n")

def	names_generator(project_name):
	names={}
	names["NAME"] = project_name
	names["CPP"] = str(project_name + '.cpp')
	names["HPP"] = str(project_name + '.hpp')
	return names

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
	print_makefile_header(file)

	# Printing components
	for component in mk_comps:
		file.write(component)
		file.write("\n\n")
	file.close()

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
	print_cpp_hpp_header(file)
	for component in hpp_comps:
		file.write(component)
	file.close()

def	cpp_generator(project_name):
	cpp_comps=[]
	include_name = '#include "' + project_name + '.hpp"\n\n'
	cpp_comps.append("int\tmain(int argc, char *argv[])\n")
	cpp_comps.append("{\n\n")
	cpp_comps.append("}\n")
	#cpp_comps.append("#endif")

	filename = str(project_name + ".cpp")
	file = open(filename, 'w')
	print_cpp_hpp_header(file)
	file.write(include_name)
	for component in cpp_comps:
		file.write(component)
	file.close()


if __name__ == '__main__':
	print('Base files for cpp generator:')
	project_name = input('\tInsert project name: ')
	names = names_generator(project_name)
	print(names)
	makefile_gen(project_name)
	hpp_generator(project_name)
	cpp_generator(project_name)

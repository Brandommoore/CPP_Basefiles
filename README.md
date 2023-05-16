# CPP_Basefiles
A basefiles generator for 42 Cpp modules.

![image](https://user-images.githubusercontent.com/29986345/196561812-204a61ce-7214-4601-ac87-9cd88d2f5f8a.png)

## Usage
This is a generator of basefiles for cpp modules. By default it generates a Makefile, a .cpp and a .hpp ready to compile.
If, for example, we only want to generate a Makefile, we would do it as follows, and so on with the rest:

	basefiles_gen.py project_name -M
	
If we want to generate only the .cpp and .hpp files:

	basefiles_gen.py project_name -C -H
	
By mcordoba (@brandommoore) with ❤

## Help
```bash
usage: basefiles_gen.py [-h] [-M] [-C] [-H] p_name

A basefiles generator for cpp modules

positional arguments:
  p_name         Project name. USAGE: [basefiles_gen.py project_name]

optional arguments:
  -h, --help     show this help message and exit
  -M, -makefile  Only generates Makefile
  -C, -cpp       Only generates Cpp
  -H, -hpp       Only generates Hpp

==================================================
```

---------------------------
# Cpp_generator
Cpp_generator is a .cpp file generator from .hpp file. Only admits .hpp files.

## Usage
This generator only admits one .hpp file. Their usage is:

	cpp_generator.py File.hpp

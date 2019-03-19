#!/usr/bin/env python3

import sys;
import os;
import glob;

# Needs Python 3.5 >= because of subprocess
if(sys.version_info < (3, 5)):
	print("This script requires python 3.5 or later. Aborting...");
	sys.exit();

import subprocess;

if(os.getuid() != 0):
	print("Please run this script with sudo. Aborting...");
	sys.exit();

try:
	bin_dir = subprocess.run(["which", "gcc"], stdout=subprocess.PIPE).stdout.decode("utf-8")[:-4];
except:
	print("Failed to get where gcc is located. Aborting...");
	sys.exit();
	
# If you wanna add more compilers, just add the default name here.
compilers = ["gcc", "gcc-ar", "gcc-nm", "gcc-ranlib", "g++", "gcov", "gcov-dump", "gcov-tool"];

for compiler in compilers:
	compiler_dir = glob.glob(bin_dir + "/" + compiler + "-[0-99]*");

	if not compiler_dir:
		print("Couldn't find any " + compiler + " alternatives.");
		continue;
	
	try:
		for c in compiler_dir:
			print("Installing " + c + " alternative for " + compiler + " with priority " + c[-1]);
			subprocess.run(["update-alternatives", "--install", bin_dir + compiler, compiler, c, c[-1]], stdout=subprocess.PIPE);
	except:
		print("Error while installing " + compiler + " alternatives. Aborting...");
		sys.exit();

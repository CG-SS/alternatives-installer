#!/usr/bin/env python3

import subprocess;
import sys;
import os;
import glob;

if(sys.version_info < (3, 5)):
	print("This script requires python 3.5 or later. Aborting...");
	sys.exit();

if(os.getuid() != 0):
	print("Please run this script with sudo. Aborting...");
	sys.exit();

try:
	bin_dir = subprocess.run(["which", "gcc"], stdout=subprocess.PIPE).stdout.decode("utf-8")[:-4];
except:
	print("Failed to get where gcc is located. Aborting...");
	sys.exit();
	

compilers = ["gcc", "gcc-ar", "gcc-nm", "gcc-ranlib", "g++", "gcov", "gcov-dump", "gcov-tool"];

for compiler in compilers:
	compiler_dir = glob.glob(bin_dir + "/" + compiler + "-[0-99]*");

	if not compiler_dir:
		print("Couldn't find any " + compiler + " alternatives.");
		continue;
	# update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 700 --slave /usr/bin/g++ g++ /usr/bin/g++-7
	try:
		for c in compiler_dir:
			print("Installing " + c + " alternative for " + compiler + " with priority " + c[-1]);
			subprocess.run(["update-alternatives", "--install", bin_dir + compiler, compiler, c, c[-1]], stdout=subprocess.PIPE);
	except:
		print("Error while installing " + compiler + " alternatives. Aborting...");
		sys.exit();

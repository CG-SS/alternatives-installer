# alternatives-installer
Script for automating the installation of GCC suit of compilers such as GCC, G++, GCOV and others.

Just run it with Python 3.5 >= and it will automatically install alternatives for GCC and others.
Normally when you self-compile GCC, most people end up only replacing GCC and forget to update other sys links such as G++ and GCOV and end up using mixed versions, such as GCC 8 with G++ 7, this will lead to unexpected behavior in the future. With this script, you can guarantee that you have the latest version as default.

You can later use sudo update-alternatives --config to see the changes.

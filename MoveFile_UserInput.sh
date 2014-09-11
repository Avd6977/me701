#!/bin/bash
# Alex Van Dyke
# Homework 1 problem 3 part b
# ME 701
# Move a user input file to the 'trash' folder in my home folder. If that folder
# does not exist, create it. If the given file does not exist, an appropriate
# error message should be printed.
# Determine how the file path is input
if [ $# -eq 0 ];
then
	# Let the user input the desired file to move
	echo "Input the file you wish to magic somewhere else"
	read UsrFile
elif [ $# -eq 1 ];
then
	UsrFile=$1
fi

# Check if that file exists
if [ -e $UsrFile ]; 
then
	echo "File found, hooray!"
else
	echo "The file was not found in the directory. Check the directory and try again or try another file. You will have to run the test again."
	echo "Thank you, goodbye."
	exit 1
fi

# Now check for the trash folder to be in the home directory
if [ -e ~/trash ];
then
	mv "$UsrFile" ~/trash
else
	mkdir ~/trash
	mv "$UsrFile" ~/trash
fi

s=${UsrFile#$(dirname "$UsrFile")/}

if [ -e ~/trash/$s ];
then	echo "Congratulations! Your file is now in the trash folder of your home directory"
else
	echo "Uh oh, something went wrong. The file is now floating somewhere else in your harddrive and this script has failed you."
fi



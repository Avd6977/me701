# Alex Van Dyke
# Homework 1 problem 3 part b
# ME 701
# Count total files in a directory

echo "Count the number of files and subdirectories in the current directory"
# echo "Enter the directory location from which you would like to count the files and subdirectories"
# read UsrDir

#ls -l "$UsrDir" | grep -c '-'
ls -l | grep -c '-'

#!/bin/bash
# Alex Van Dyke
# Homework 1 problem 3 part a
# ME 701
# Convert degrees Fahrenheit to degrees Celcius

# Determine how the degF temperature is input
if [ $# -eq 0 ];
then
	echo "Convert degrees Fahrenheit into degrees Celcius"
	echo "Input degrees Fahrenheit you wish to convert"
	read degF
elif [ $# -eq 1 ];
then
	degF=$1
fi

declare degC
degC=$(bc <<< "("$degF"-32)*0.5555")
Kelvin=$(bc <<< $degC"+273.15")
if [ $Kelvin '<' 0 ]; then
	echo "This temperature is invalid, must be above absolute 0"
else
	echo "Celcius = " $degC
	echo "Kel = "$Kelvin
fi

#!/bin/bash
# Alex Van Dyke
# Homework 1 problem 3 part a
# ME 701
# Convert degrees Fahrenheit to degrees Celcius

echo "Convert degrees Fahrenheit into degrees Celcius"
echo "Input degrees Fahrenheit you wish to convert"
read degF

declare degC
let "degC = (degF - 32) * 5 / 9"

echo "Celcius = " $degC

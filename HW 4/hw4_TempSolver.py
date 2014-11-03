# Test of the F2PY module

from hw4 import *

print "Dirilicht conditions (temperature at both sides defined)"
tempsolver.tempsolve(1, 1, 100, 0, 100, 0, 0)
print "\n"
print "Left side temperature and spatial derivative defined"
tempsolver.tempsolve(1.5, 2, 500, 1.5, 0, 0, 1)
print "\n"
print "Right side temperature and spatial derivative defined"
tempsolver.tempsolve(2.05, -4, 0, 0, 290, -5, 2)

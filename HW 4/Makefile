all: hw4

# F2PY for hw4
hw4:
	f2py2.7 -c -m $@ ModuleTempSolver.f90

# Remove objects, module files, and exectables
clean:
	@rm -f *.o *.mod *-x *wrap.cxx *.so

# Same, but leave the shared objects
neat:
	@rm -f *.o *.mod *-x *wrap.cxx

#===============================================================================
# Rules
#===============================================================================

.SUFFIXES: .f90 .o
.PHONY: clean neat

%.o: %.f90
	$(F90) $(F90FLAGS) $(INCLUDE) -c $<

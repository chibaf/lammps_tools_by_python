#!/usr/bin/python 
#
#	uo2 on fcc 110 face
#

#
#	importing python libraries
#
import sys
from string import *
from math import *

#
#  generating lammps data with staggered arrangement
#

# parameters
uranium="1"   # atom type in lammps script
oxygen="2"    # atom type in lammps script
charge=2.4
charge_uranium=str(charge) # charge of uranium
charge_xenon=str(-charge/2.) # charge of oxygen
#
mx=8; # number of oxygens in x-direction
my=8; # number of oxygens in y-direction
mz=8; # number of oxygens in z-direction
#
A=5.47 # lattice parameter
a=A/2.0 # lattice parameter
b=a*sqrt(2.0)

# generating coordinates of uranuims with staggered arrangement
list_atoms=[]
number_uranium=0 # index of atoms
for k in range(0,mz): # z-direction
 for j in range(0,my/2): # y-direction
  for i in range(0,mx): # x-direction
   number_uranium=number_uranium+1
   x=i*b+k*b/2.0; x=fmod(x,mx*b)
   y=j*a*2+k*a; y=fmod(y,my*a)
   z=k*b/2.0
   el=[number_uranium,uranium,charge_uranium,x,y,z]
   list_atoms.append(el)

# generating coordinates of oxygens
number_oxygen=number_uranium
for k in range(0,mz): # index in z-direction
 for j in range(0,my): # index in  y-direction
  for i in range(0,mx): # index in  x-direction
   number_oxygen=number_oxygen+1
   x=i*b+(k+1)*b/2.0; x=fmod(x,b*mx)
   y=j*a+a/2.0
   z=k*b/2.0
   el=[number_oxygen,oxygen,charge_xenon,x,y,z]
   list_atoms.append(el)
number_oxygen=number_oxygen-number_uranium

#
# printing lammps data
#
f=sys.stdout    # use standard i/o
#
f.write("UO2 on FCC 110 face: U"+str(number_uranium)+"O"+str(number_oxygen)+" \n") # header
f.write("\n")
f.write(str(len(list_atoms))+" atoms\n")  # number of atoms
f.write("\n")
f.write("0 bonds\n")          # lammps parameter
f.write("0 angles\n")         # lammps parameter
f.write("0 dihedrals\n")      # lammps parameter
f.write("0 impropers\n")      # lammps parameter
f.write("\n")
f.write("2 atom types\n")     # number of atom types
f.write("0 bond types\n")     # lammps parameter
f.write("0 angle types\n")    # lammps parameter
f.write("0 dihedral types\n") # lammps parameter
f.write("0 improper types\n") # lammps parameter
f.write("\n")
f.write("\n")
# range of box
f.write(join((str(0),str(b*mx),"xlo xhi\n")))     # length of box for x direction
f.write(join((str(0),str(a*my),"ylo yhi\n")))     # length of box for x direction
f.write(join((str(0),str(b*mz/2.0),"zlo zhi\n"))) # length of box for x direction
f.write("\n")
f.write("\n")
# printing coordinates of atoms
f.write("Atoms\n")
f.write("\n")
for i in range(0,len(list_atoms)):
 el=list_atoms[i]
 el=[str(el[0]),el[1],el[2],str(el[3]),str(el[4]),str(el[5]),"\n"]
 s=join(el)
 f.write(s)

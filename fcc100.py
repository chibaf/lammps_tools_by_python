#!/usr/bin/python 
#
#	uo2 on fcc 100
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
uranium="1"
oxygen="2"
charge=2.4
charge1=str(charge) # charge of uranium
charge2=str(-charge/2.) # charge of oxygen

mx=8; # number of oxygens in x-direction
my=8; # number of oxygens in y-direction
mz=8; # number of oxygens in z-direction

a=5.47 # lattice parameter
b=a/2.0
c=a/4.0

# generating coordinates of uranuims with staggered arrangement
list_atoms=[]
icnt=0 # index of atoms
for k in range(1,mz+1): # index for z-direction
 for j in range(1,my+1): # index for y-direction
  for i in range(1,mx/2+1): # index for x-direction
   icnt=icnt+1
   if fmod(k,2)==1:
    if fmod(j,2)==1:
     el=[icnt,uranium,charge1,(i-1)*a,j*b,(k-1)*b]
     list_atoms.append(el)
    else:
     el=[icnt,uranium,charge1,b+(i-1)*a,j*b,(k-1)*b]
     list_atoms.append(el)
   else:
    if fmod(j,2)==1:
     el=[icnt,uranium,charge1,b+(i-1)*a,j*b,(k-1)*b]
     list_atoms.append(el)
    else:
     el=[icnt,uranium,charge1,(i-1)*a,j*b,(k-1)*b]
     list_atoms.append(el)
num_of_uranium=icnt
#
# generating coordinates of oxygens
icnt=num_of_uranium
for k in range(1,mz+1): # index for z-direction
 for j in range(1,my+1): # index for y-direction
  for i in range(1,mx+1): # index for x-direction
   icnt=icnt+1
   el=[icnt,oxygen,charge2,c+(i-1)*b,c+(j-1)*b,c+(k-1)*b]
   list_atoms.append(el)
num_of_oxygen=icnt-num_of_uranium

#
# printing lammps data
#
fw=sys.stdout
#
fw.write("UO2 with staggered arrangement: U"+str(num_of_uranium)+"O"+str(num_of_oxygen)+" \n")
fw.write("\n")
fw.write(str(len(list_atoms))+" atoms\n")
fw.write("\n")
fw.write("0 bonds\n")
fw.write("0 angles\n")
fw.write("0 dihedrals\n")
fw.write("0 impropers\n")
fw.write("\n")
fw.write("2 atom types\n")
fw.write("0 bond types\n")
fw.write("0 angle types\n")
fw.write("0 dihedral types\n")
fw.write("0 improper types\n")
# range of box
fw.write("\n")
fw.write("\n")
fw.write(join((str(0),str(b*mx),"xlo xhi\n")))
fw.write(join((str(0),str(b*my),"ylo yhi\n")))
fw.write(join((str(0),str(b*mz),"zlo zhi\n")))
fw.write("\n")
fw.write("\n")
# printing sets of coordinates of atoms
fw.write("Atoms\n")
fw.write("\n")
for l in range(0,len(list_atoms)):
 el=list_atoms[l]
 el=[str(el[0]),el[1],el[2],str(el[3]),str(el[4]),str(el[5]),"\n"]
 s=join(el)
 fw.write(s)

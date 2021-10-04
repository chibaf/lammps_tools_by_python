#!/usr/bin/python 

#
#	functions defied by user
#
def isReal(txt):
    try:
        float(txt)
        return True
    except ValueError:
        return False

#
#	importing python libraries
#
import sys
from string import *

#
#  reading lammps data (input)
#
fi=sys.stdin

atom_list = []
atmflg=0

for line in fi.readlines():
# separating numbers with single space if needed
 if line != "\n":
  ret=line.find("-")
  if ret>=0:
   eret=line.find("e-")
   if eret<0:
    line=line.replace("-"," -")
# find number of atoms
  ret=line.find("atoms")
  if ret>=0:
   split=str.split(line)
   anumber=split[0]
# box range (x)
  ret=line.find("xlo")
  if ret>=0:
   split=str.split(line)
   xlo=float(split[0])
   xhi=float(split[1])
# box range (y)
  ret=line.find("ylo")
  if ret>=0:
   split=str.split(line)
   ylo=float(split[0])
   yhi=float(split[1])
# box range (z)
  ret=line.find("zlo")
  if ret>=0:
   split=str.split(line)
   zlo=float(split[0])
   zhi=float(split[1])
# find coordinates of atoms
  ret=line.find("Atoms")
  if ret>=0:
   atmflg=1
  if atmflg==1:
   split=str.split(line)
#-----------> start
#
#   REMARK: this part needs to be modified with your lammps setting.
#
   if len(split)>5: # 2011-04-17
    if split[1]=="1":
     atomic_weight="234"
     atomic_name="U"
    elif split[1]=="2":
     atomic_weight="016"
     atomic_name="O"
    elif split[1]=="3":
     atomic_weight="050"
     atomic_name="Cu"
    elif split[1]=="4":
     atomic_weight="010"
     atomic_name="Bo"
    else: # 2011-04-17
     atomic_weight="000" # 2011-04-17
     atomic_name="?" # 2011-04-17
#-----------> end
# the box is supposed to be a rectangular parallelepiped.
    x=(float(split[3])-xlo)/(xhi-xlo) # 2011-04-17
    y=(float(split[4])-ylo)/(yhi-ylo) # 2011-04-17
    z=(float(split[5])-zlo)/(zhi-zlo) # 2011-04-17
    el=[atomic_weight,atomic_name,str(x),str(y),str(z),"0","0","0"]
    atom_list.append(el)
     
#
# printing cfg file (output) - for atomeye
#
fw=sys.stdout

fw.write("Number of particles =   "+anumber+" \n")
fw.write("#\n")
fw.write("\n")
fw.write("A = 1.0 Angstrom\n")
fw.write("#\n")
fw.write("\n")
fw.write(" H0(1,1) =   "+str(xhi-xlo)+" A\n") # 2011-04-17
fw.write(" H0(1,2) = 0 A\n")
fw.write(" H0(1,3) = 0 A\n")
fw.write("#\n")
fw.write("\n")
fw.write(" H0(2,1) = 0 A\n")
fw.write(" H0(2,2) =   "+str(yhi-ylo)+" A\n") # 2011-04-17
fw.write(" H0(2,3) = 0 A\n")
fw.write("#\n")
fw.write("\n")
fw.write(" H0(3,1) = 0 A\n")
fw.write(" H0(3,2) = 0 A\n")
fw.write(" H0(3,3) =   "+str(zhi-zlo)+" A\n") # 2011-04-17
fw.write("#\n")
fw.write("\n")
fw.write("eta(1,1) = 0\n")
fw.write("eta(1,2) = 0\n")
fw.write("eta(1,3) = 0\n")
fw.write("eta(2,2) = 0\n")
fw.write("eta(2,3) = 0\n")
fw.write("eta(3,3) = 0\n")
fw.write("#\n")
fw.write("\n")
fw.write("#\n")
fw.write("#\n")
fw.write("#\n")
fw.write("\n")
fw.write("#\n")
fw.write("#\n")
fw.write("#\n")
fw.write("#\n")
fw.write("\n")
fw.write("#\n")
fw.write("#\n")
fw.write("#\n")
fw.write("\n")

#printing atoms coordinates
for i in range(0, len(atom_list)):
 el=atom_list[i]
 s=join((el[0],el[1],el[2],el[3],el[4],el[5],el[6],el[7],"\n"))
 fw.write(s)
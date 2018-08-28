#!/usr/bin/env python
# -*- coding: utf-8 -*-

#grafos podem ser uteis para analisar liquidos.
import string
from sys import argv
import numpy as np
import re
#import aplotter
#import Gnuplot as gplot

" e_getOPTsteps.py gaussianout.log\n"


def readNlines(fileobj,number_of_lines):
  """
  read N lines and return the last one
  """
  
  for n in range(number_of_lines):
    new_line = fileobj.readline()
  
  return new_line

#Comando de exemplo:
#getnmr.py gaussianout.log tag_graphs  natm

#according to wikipedia ...
au2kJmol = 2625.50
kT_kJmol = 0.00831446*298.15


au2ev = 27.211396
kT_ev  = 0.0257 #eV

elements = {1:'H',6:'C',7:'N',8:'O',9:'F',11:'Na',12:'Mg',15:'P',16:'S',17:'Cl',26:'Fe',29:'Cu',30:'Zn',54:'Xe'}

#COLORS
RED = "\033[91m"
BLUE = "\033[94m"
END = "\033[0m"

fname = argv[1]


finp = open(fname,'r')

temp = re.split('\.',fname)

nameout = temp[0]

output_traj = nameout + "_traj.xyz"
output_opt = nameout + "_opt.xyz"
traj_xyz = open(output_traj,'w')
opt_xyz = open(output_opt,'w')
#step_xyz = open("OPT_step_"+str(nstep)+".xyz",'w') 
#dadosE = open("scf_energies.dat",'w')

energy = []


n = 0

line = finp.readline()

print BLUE + "Opt procedure:" +END



while line:
    #lines = finp.readlines(100000)
    if not line:
        break
    ln = line[:-1]
    if ln.count("SCF Done:") == 1:
	  
	  #print ln
	  i = ln.find("=")
	  i_end = ln.find("A.U")
	  
	  #Shielding Magnetico
	  #=  -2196.37551036
	  
	  E = float(ln[i+1:i_end-1])*au2kJmol
	  
	  #print "SCF Energy = %.3f kJ/mol" %(E)
	  energy.append(E)
	  
	          
          #print "%3d\t%.3f\n" %(n,sh)
          #dadosE.write("%3d\t%.3f\n" %(n,E))
    if ln.count(" Input orientation") == 1 and len(energy)>0:
      to_print = []
      ln = readNlines(finp,5)
      comment =  "Step %3d" %n + "  (E-E0) ="+BLUE+" %13.7f" %(E - energy[0]) +END+" kJ/mol"
      comment2 =  "Step %3d (E-E0)  %13.7f  kJ/mol" %(n,E - energy[0]) 
      n+=1
      print comment
      to_print.append(comment2+"\n")
      while ln.count('---')==0:
	  cols = re.split("\s+",ln)
	  #print cols
	  Z = int(cols[2])
	  x,y,z = map(float,cols[4:7])
	  fmt_xyz = "%-4s    %11.6f%11.6f%11.6f\n"
	  #print fmt_xyz %(elements[Z],x,y,z)
	  atom_line = fmt_xyz %(elements[Z],x,y,z)
	  #print atom_line
	  to_print.append(atom_line)
	  ln = finp.readline()
      Natoms =len(to_print) - 1
      
      #opt_xyz.close()
      #opt_xyz = open(output_traj,'w')
      #traj_xyz.write('  %d\n' %Natoms)
      #opt_xyz.write('  %d\n' %Natoms)
      #for l2p in to_print:
	#traj_xyz.write(l2p)
	#opt_xyz.write(l2p)
      #if n==nstep:
	  #print n,ln

	


    line = finp.readline()
    #n+=1

opt_xyz.write('  %d\n' %Natoms)
for l2p in to_print:
    opt_xyz.write(l2p)
    
#Fim da leitura - Calculo de Medias
Enr = np.array(energy) - np.min(energy)

Ef = energy[-1]
print 
print BLUE+"Final Energy:"+END
print "%.9f  Hartree,  %.7f  kJ/mol\n\n" %(Ef/au2kJmol,Ef)

#print
#print 'E - Emin (kJ/mol):'
#print Enr
#print
x = Enr/kT_kJmol

#print x

Q=sum(np.exp(-x))

#print "Partition Function Q:"
#print Q
#print

Prob = np.exp(-Enr/kT_kJmol)/Q
print BLUE+"Probabilities (%):"+END
print 100*Prob,"sum = ",100*sum(Prob)


print 
print RED+ "Output: %s" %output_opt +END
print




from ase.lattice.hexagonal import *
import ase.io as io
from ase import Atoms, Atom
from ase.neighborlist import NeighborList, natural_cutoffs
import copy
import numpy as np 

index1 = 5
index2 = 6
mya    = 2.46
myc    = 6.70 

stacks = 5 

gra = Graphite(symbol = 'C',latticeconstant={'a':mya,'c':myc},
               size=(index1,index2,stacks))
io.write('graphite_large.xyz', gra, format='extxyz')


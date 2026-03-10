from ase.lattice.hexagonal import *
import ase.io as io
from ase import Atoms, Atom
from ase.neighborlist import NeighborList, natural_cutoffs
import copy
import numpy as np 

index1 = 4
index2 = 3
mya    = 2.46
myc    = 6.70 

stacks = 2 

gra = Graphite(symbol = 'C',latticeconstant={'a':mya,'c':myc},
               size=(index1,index2,stacks))
io.write('graphite.xyz', gra, format='extxyz')

# Now modify this with some oxygen 

nc = len( gra )
no = int( nc / 3 ) + 1 
n_tot = nc + no 
o_c_ratio = no / nc 

px  = gra.cell[0]
py  = gra.cell[1]
pz  = gra.cell[2]

atoms = copy.deepcopy( gra )
trial_atoms = copy.deepcopy( atoms )

dist_tol = 1.0

for i in range( no ): 
   inserted_O = False 
   tried_O = False 
   atoms_prev = copy.deepcopy( trial_atoms )

   while ( not inserted_O ): 
        r3 = np.random.random_sample( (3,) )
        position = px * r3[0] + py * r3[1] + pz * r3[2]
        
        if ( not tried_O ): 
           new_atom = Atom( 'O', position = position  ) 
           trial_atoms.append( new_atom )
           tried_O = True
        else: 
           trial_atoms.position[-1] = position
        
        distances = atoms_prev.get_distances( trial_atoms, len(trial_atoms) - 1, mic=True )

        if ( any( distances < dist_tol ) ): 
           continue 
        else: 
            inserted_O = True
            atoms = copy.deepcopy( trial_atoms )


io.write('atoms.xyz', atoms, format='extxyz')

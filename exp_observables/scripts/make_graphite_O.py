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

stacks = 1 

gra = Graphite(symbol = 'C',latticeconstant={'a':mya,'c':myc},
               size=(index1,index2,stacks))
io.write('graphite.xyz', gra, format='extxyz')

# Now modify this with some oxygen 

nc = len( gra )
no = int( nc / 3 ) + 1 
n_tot = nc + no 
o_c_ratio = no / nc 

print( f"Cell will have {nc} carbon atoms and {no} oxygen atoms, with O:C ratio of {o_c_ratio}")

px  = gra.cell[0]
py  = gra.cell[1]
pz  = gra.cell[2]

atoms = copy.deepcopy( gra )

min_dist = 1.0

for i in range( no ): 
   inserted_O = False 

   while ( not inserted_O ): 
        r3 = np.random.random_sample( (3,) )
        position = px * r3[0] + py * r3[1] + pz * r3[2]

        temp_atoms = atoms + Atoms('O', positions=[position])
        
        # 2. Check distances
        # Get neighbors within min_dist
        cutoffs = [min_dist / 2.0] * len(temp_atoms)
        nl = NeighborList(cutoffs, self_interaction=False, 
                                        bothways=True)
        nl.update(temp_atoms)
        
        # Check if the new atom (last in list) has any neighbors
        indices = nl.get_neighbors(len(temp_atoms) - 1)[0]
        if len(indices) == 0:
            inserted_O = True
            atoms = temp_atoms
            print( f"added O atom {i:3d} at ", position)
        else: 
            continue


io.write('atoms.xyz', atoms, format='extxyz')

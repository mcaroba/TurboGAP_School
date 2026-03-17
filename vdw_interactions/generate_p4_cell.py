from ase.io import write
from ase import Atoms
import numpy as np
from ase.build import make_supercell

n_mols = 27
rho = 0.02

d0 = 2.206
a0 = np.sqrt(2.)*d0
a = 4.9

pos = [[0., 0., 0.],
       [0., a0/2., a0/2.],
       [a0/2., 0., a0/2.],
       [a0/2., a0/2., 0.]]
atoms0 = Atoms("P4", positions=pos, cell=[a,a,a], pbc=True)
atoms0.center()

n_cells = (n_mols)**(1./3.)

if int(n_cells)**3 != n_mols:
    n_cells = int(n_cells) + 1
else:
    n_cells = int(n_cells)

P = np.diag([n_cells,n_cells,n_cells])
atoms = make_supercell(atoms0,P)


L = (30.97*n_mols*4*1.60217663 / rho)**(1./3.)
atoms.set_cell([L,L,L])

atoms.set_array("velocities", 0.01*(np.random.sample([len(atoms), 3])-0.5))


write("p4_cell.xyz", atoms)


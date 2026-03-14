from ase.io import write
from ase import Atoms
import numpy as np


for deg in np.arange(0,181,2,dtype='float'):

    d0 = 2.206
    a0 = np.sqrt(2.)*d0
    a = 4.9

    L = 50.0

    pos = [[0., 0., 0.],
           [0., a0/2., a0/2.],
           [a0/2., 0., a0/2.],
           [a0/2., a0/2., 0.]]
    atoms = Atoms("P4", positions=pos, cell=[a,a,a], pbc=True)
    atoms.center()

    atoms.set_cell([L,L,L])
    atoms.positions += np.array([L/2-2.5,L/2,L/2])

    atoms.set_array("velocities", 0.01*(np.random.sample([len(atoms), 3])-0.5))

    atoms.euler_rotate(deg,0,0,center='COM')


    pos = [[0., 0., 0.],
           [0., a0/2., a0/2.],
           [a0/2., 0., a0/2.],
           [a0/2., a0/2., 0.]]
    atoms2 = Atoms("P4", positions=pos, cell=[a,a,a], pbc=True)
    atoms2.center()

    atoms2.set_cell([L,L,L])
    atoms2.positions += np.array([L/2+2.5,L/2,L/2])

    atoms2.set_array("velocities", 0.01*(np.random.sample([len(atoms), 3])-0.5))


    if ( deg == 0.):
        write("p4_dimer.xyz", atoms+atoms2)
    else:
        write("p4_dimer.xyz", atoms+atoms2, append=True)
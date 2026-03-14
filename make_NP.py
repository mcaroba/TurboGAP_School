import numpy as np
from ase.io import write
from ase import Atoms

a = 3.9
d_min = 2.

n = 79
c_Au = 0.5

R = (a**3 / 4. * n * 3./4./np.pi)**(1./3.)
pos = []
while len(pos) < n:
    this_pos = (2.*np.random.sample([3]) -1) * R
    d = np.dot(this_pos, this_pos)**0.5
    if d > R:
        continue
    if len(pos) == 0:
        pos.append(this_pos)
    else:
        too_close = False
        for other_pos in pos:
            dv = this_pos - other_pos
            d = np.dot(dv, dv)**0.5
            if d < d_min:
                too_close = True
                break
        if not too_close:
            pos.append(this_pos)

n_Au = int(n*c_Au)
n_Pd = n - n_Au

atoms = Atoms("Au%iPd%i" % (n_Au, n_Pd), positions = pos, pbc=True)
atoms.center(vacuum = 12.)

vel = 0.01 * (np.random.sample([len(atoms),3])-0.5)
atoms.set_array("vel", vel)

write("structures/atoms0.xyz", atoms)

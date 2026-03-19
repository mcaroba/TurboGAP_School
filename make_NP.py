##################################################################
# This script generates an initial atomic structure for melt-quench
# simulations. It will generate an Au-Pd nanoparticle with random
# distributions of atoms with roughly spherical shapes.
##################################################################

##################################################################
import numpy as np
from ase.io import write
from ase import Atoms
##################################################################

##################################################################
# Input variables - you can change c_Pd and n in the last part of
# this hands-on session
#
# Lattice parameters for pure metals (Angstroms, FCC)
a_Au = 4.0782
a_Pd = 3.8898

# Concentration of palladium atoms
c_Pd = 0.5
c_Au = 1 - c_Pd

# Effective lattice parameter via Vegard's Law (linear interpolation)
a = a_Au * c_Au + a_Pd * c_Pd  # = 3.9840 Angstroms for Au50Pd50

# Minimum allowed distance between any two atoms (Angstroms)
d_min = 2.
# Total number of atoms in the nanoparticle
n = 55
##################################################################

##################################################################
# Nanoparticle construction
#
# Estimate the radius of the nanoparticle sphere based on FCC packing density
# Using: volume of sphere = n * (volume of FCC unit cell / 4 atoms per cell)
R = (a**3 / 4. * n * 3./4./np.pi)**(1./3.)

# List to store accepted atomic positions
pos = []

# Keep generating random positions until we have n atoms placed
while len(pos) < n:
    # Generate a random 3D position within a cube of side 2R, centered at origin
    this_pos = (2.*np.random.sample([3]) - 1) * R

    # Compute distance from the origin
    d = np.dot(this_pos, this_pos)**0.5

    # Reject the position if it lies outside the sphere of radius R
    if d > R:
        continue

    # If no atoms placed yet, accept the first position unconditionally
    if len(pos) == 0:
        pos.append(this_pos)
    else:
        too_close = False
        # Check distance to all already-placed atoms
        for other_pos in pos:
            dv = this_pos - other_pos
            d = np.dot(dv, dv)**0.5
            # Reject if closer than the minimum allowed distance
            if d < d_min:
                too_close = True
                break
        # Only accept the position if it's not too close to any existing atom
        if not too_close:
            pos.append(this_pos)

# Calculate the number of Au and Pd atoms based on the concentration
n_Pd = int(n * c_Pd)       # Number of palladium atoms
n_Au = n - n_Pd            # Number of gold atoms

# Create the ASE Atoms object with the generated positions
atoms = Atoms("Au%iPd%i" % (n_Au, n_Pd), positions=pos)

# Add vacuum padding of 5 Angstroms around the cluster (isolates it in the cell)
atoms.center(vacuum=5.)

# Generate small random initial velocities for each atom (for MD simulations) in Angstrom/fs
vel = 0.01 * (np.random.sample([len(atoms), 3]) - 0.5)
atoms.set_array("vel", vel)

# Write the atomic structure to an XYZ file for visualization
write("structures/atoms0.xyz" , atoms)
##################################################################

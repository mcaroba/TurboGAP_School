##################################################################
# This code generates the initial atomic structure for the carbon
# melt-quench simulation
##################################################################

##################################################################
# Some package imports
import numpy as np
from ase.io import write
from ase import Atoms
##################################################################

##################################################################
# Input variables - the user can change these, but be mindful of
# the choices!
N = 30 # number of atoms in the simulation box
rho = 1. # (initial) density in g/cm3 - this can change if barostatting is used
T0 = 9000. # (initial) temperature in K - this determines random velocities
##################################################################

##################################################################
# Structure construction - only change this if you know what
# you're doing
vol = (N * 12.01 * 1.660539)/rho # volume in Angstron^3
L = vol**(1./3.) # side of simulation cell assuming a cube
cell = np.array([L, L, L])

# Random positions
# positions = np.random.sample([N, 3]) # this is easy/tempting but dangerous (do you know why?)
# this is not dangerous:
NI = int(np.ceil(N**(1./3.)))
line = np.arange(0., 1., 1./NI)
grid = np.vstack(np.meshgrid(line, line, line)).reshape(3,-1).T
np.random.shuffle(grid)
positions = grid[0:N]
for pos in positions:
    pos *= cell

# Random velocities (TurboGAP uses Angstrom/fs as velocity units)
velocities = np.random.sample([N, 3]) - 0.5
e_kin_target = 3./2. * 1.380649e-23 * (N-1) * T0 # target kinetic energy in J from equipartition theorem and subtracting CM DoF
e_kin = 1./2. * 12.01 * 1.660539e-27 * np.sum([np.dot(vel,vel) for vel in velocities]) * 1.e-20/1.e-30 # current kinetic energy in J
velocities *= np.sqrt(e_kin_target/e_kin)

atoms = Atoms("C%i" % (N), cell = cell, positions = positions, pbc = True)
atoms.set_array("velocities", velocities)

write("atoms0.xyz", atoms)
print("Structure generated!")
##################################################################

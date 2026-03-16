from pymatgen.analysis.diffraction.xrd import XRDCalculator
from pymatgen.core import Lattice, Structure
from pymatgen.io.ase import AseAtomsAdaptor
from ase.io import read
import numpy as np 
from ase.lattice.hexagonal import *
import matplotlib.pyplot as plt

# Using CuKalpha radiation 
CuKa = 1.54184 # Angstrom 
def q_to_twotheta( q, wavelength=CuKa ):
    return 2 * np.arcsin( q * wavelength / (4.0 * np.pi) ) * 180.0 / np.pi

def twotheta_to_q( twotheta, wavelength=CuKa ):
    return 4 * np.pi * np.sin( twotheta / 2.0 * np.pi / 180.0 ) / wavelength

index1 = 1
index2 = 1
mya    = 2.46
myc    = 6.70 

stacks = 1 

gra = Graphite(symbol = 'C',latticeconstant={'a':mya,'c':myc},
               size=(index1,index2,stacks))

atoms = gra #read( "structures/graphite_large.xyz", format ="extxyz" ) 


structure = AseAtomsAdaptor.get_structure( atoms )

c = XRDCalculator()

ax = c.get_plot(structure)

locs = ax.get_xticks()
new_locs_q = sorted( set([ int( twotheta_to_q( loc ) ) for loc in locs   ] ) )
labels = [ str(loc) for loc in new_locs_q ]
new_locs_twotheta = [ q_to_twotheta( loc ) for loc in new_locs_q ]
ax.set_xticks( new_locs_twotheta, labels )

ax.set_xlabel("q [1/A]")
plt.show()

from ase.io import read
from ase.geometry.analysis import Analysis
import matplotlib.pyplot as plt
import numpy as np

first = read("p4_md_equil.xyz")
last = read("p4_last.xyz")
ana = Analysis(first)
rdf = ana.get_rdf(rmax=10,nbins=101)
r = np.linspace(0,20,101)
plt.figure()
plt.plot(r,rdf[0],'b-')
plt.show()
ana = Analysis(last)
rdf = ana.get_rdf(rmax=10,nbins=101)
r = np.linspace(0,20,101)
plt.figure()
plt.plot(r,rdf[0],'b-')
plt.show()

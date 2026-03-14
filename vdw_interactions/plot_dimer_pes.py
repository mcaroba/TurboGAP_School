import numpy as np
import matplotlib.pyplot as plt

ts = np.loadtxt("energy_ts.dat")
mbd = np.loadtxt("energy_mbd.dat")
deg = np.arange(0,181,2)

plt.figure()
plt.plot(deg,ts,'b.-',label="TS")
plt.plot(deg,mbd-mbd[0]+ts[0],'r.-',label="MBD")
plt.legend()
plt.xlabel("Rotation in degrees")
plt.ylabel("Dispersion energy [eV]")
plt.title("P4 dimer PES for rotation of one molecule")
plt.show()

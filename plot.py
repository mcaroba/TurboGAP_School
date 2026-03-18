import matplotlib.pyplot as plt
import numpy as np

N = 79

fig, axs = plt.subplots(1, 2, figsize=(8, 4), layout='constrained')

data = np.genfromtxt('thermo.log')
nsteps = data[:, 0]
ener   = data[:, 4]

axs[0].plot(nsteps, ener)
axs[0].set_ylabel('energy (eV)')



plt.show()
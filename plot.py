import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(1, 2, figsize=(8, 4), layout='constrained')

data = np.genfromtxt('mc.log')
nsteps = data[:, 0]
ener   = data[:, 4]
ntot   = data[0, 5]
cH   = data[:, 7]

axs[0].plot(nsteps, ener)
axs[0].set_ylabel('energy (eV)')
axs[0].set_xlabel('MC steps')

axs[1].plot(nsteps, cH/ntot)
axs[1].set_ylabel('cH (%)')
axs[1].set_xlabel('MC steps')

plt.show()
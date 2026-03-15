import matplotlib.pyplot as plt
import numpy as np

N = 79

fig, axs = plt.subplots(1, 2, figsize=(8, 4), layout='constrained')

data = np.genfromtxt('mc.log')
nsteps = data[:, 0]
ener   = data[:, 4]
cH     = data[:, 7]

axs[0].plot(nsteps, ener)
axs[0].set_ylabel('energy (eV)')

axs[1].plot(nsteps, cH/N)
axs[0].set_ylabel('cH')
for i in range(1, 2):
    axs[i].set_xlabel('mc steps')


plt.show()
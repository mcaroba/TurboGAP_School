import matplotlib.pyplot as plt
import numpy as np


fig, axs = plt.subplots(1, 2, figsize=(8, 4), layout='constrained')

data = np.genfromtxt('mc.log')
nsteps = data[:, 0]
ener   = data[:, 4]
cH     = data[:, 7]

axs[0].plot(nsteps, ener)
axs[1].plot(nsteps, cH/79)

plt.show()
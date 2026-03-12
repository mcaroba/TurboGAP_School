#!/usr/bin/env python
# coding: utf-8

# ### 1. Introduction to Threshold Displacement Energy (TDE)
# 
# **Threshold Displacement Energy (TDE)** is a fundamental parameter used to quantify radiation damage in materials. It is defined as the **minimum kinetic energy** required to displace an atom from its equilibrium lattice site and create a **stable defect**.
# 
# TDE is highly sensitive to the crystallographic direction, with significant variations observed even between closely spaced orientations. Furthermore, defect generation is **non-monotonous** [Nordlund, Kai et al. NIMB 246, no.2 (2006) 322-332]. This means that increasing the energy does not always guarantee a defect will form, as higher energies may trigger immediate recombination.
# 
# <div style="text-align: center;">
#     <img src="nonMonotonous_TDE.png" alt="TDE Non-monotony" width="400">
#     <p><i>Fig 1: Non-monotonous defect formation probability (Nordlund et al.)</i></p>
# </div>
# 
# ---
# 
# ### 2. Methodology: Calculating TDE via Molecular Dynamics (MD)
# 
# To determine the TDE in a specific direction using the **TurboGAP** code, we employ the following iterative procedure:
# 
# 1. **Initialization:** The simulation begins by assigning an **initial "low" PKA energy** to a specific atom. After a brief interval (e.g., 1–2 ps for Silicon), the system is checked for defects. This duration allows the PKA to complete its initial collision cascade.
# 2. **Stability Verification:** If a defect is detected, the simulation continues until a relaxation time $T_r$ (e.g., 10 ps) is reached. This ensures that the defect is truly stable and does not get **recombined**.
# 3. **Iteration:** If no stable defect is identified, the simulation is reset with a **PKA energy increment** ($\Delta E$). This process repeats until the first stable defect is successfully identified.
# 
# ---
# 
# ### 3. Implementation Details
# 
# In this tutorial, we implement the TDE calculation through a Python workflow. 
# 
# The implementation follows three main phases:
# 
# * **Phase 1: Cell Equilibration** We begin by thermalizing Silicon supercell at a target temperature. This ensures the lattice contains realistic thermal displacements and velocities before the impact event occurs.
#     
# * **Phase 2: PKA Selection and Velocity Initialization** A specific atom is designated as the **PKA**. Based on the chosen crystallographic direction, we calculate the velocity components $(v_x, v_y, v_z)$ required to match the target PKA energy in electronvolts (eV).
#     
# * **Phase 3: MD Execution and Defect Analysis** The dynamics are launched. After the simulation, we visually check the trajectory to determine if a stable defect has been created. If no defect is found, the simulation should be run with the $E+\Delta E$ PKA energy.
# 

# In[1]:


from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.velocitydistribution import Stationary
from weas_widget import WeasWidget
from ase.build import bulk
from ase.io import write, read
import numpy as np
import math
import subprocess
import matplotlib.pyplot as plt


# In[2]:


# The following functions will be used throughout the notebook.
# The first visualizes structures and trajectories, and the
# second runs the TurboGAP code.

def visualize(atoms):
    """
    Visualize the given structure or trajectory.

    Parameters:
        ASE's atoms object

    Returns:
        'viewer', the visual handle of the given object
    """
    viewer = WeasWidget()
    viewer.avr.model_style = 0 # ball mode
    viewer.from_ase(atoms)
    viewer.avr.species.settings["Si"].update({"radius": 0.5})
    return viewer


def run_turbogap(n_cores=8):
    """
    Run the TurboGAP code in 'md' mode (turbogap md).
    The 'input' file and 'gap_files/' directory should be present
    in the working directory. 
    """
    command = ['mpirun', '-np', str(n_cores), 'turbogap', 'md']
    result = subprocess.run(command, check=True)


# In[3]:


# Creating the pristine cell:

ao = 5.467 #the optimum lattice constant predicted by the poential
element = 'Si'
lattice = 'diamond'
rx, ry, rz = 3, 3, 3 

atoms_pristine = bulk(element, lattice, ao, cubic=True)
atoms_pristine = atoms_pristine.repeat([rx, ry, rz])

pcell = 'pristine.xyz'
write(pcell, atoms_pristine)

viewer = visualize(atoms_pristine); viewer


# In[ ]:


# Thermalizing the cell at the given temperature. Thermalization is done to
# make the simulation results comparable with experimental values measured at
# the same temperature. Also, the random motion of atoms creates a more realistic
# collision probability between the lattice atoms and the atom in motion.

def create_tgap_input_eq(cell_name, temp, md_nsteps):
    """
    Creates TurboGAP input file to run NPT.

    Parameters:
        cell_name : structure file in xyz format
        temp      : temperature
        md_nsteps : number of steps
    
    Returns:
        the 'input' file is written in the directory
    """
    input_str = f"""! Species-specific info
    atoms_file = '{cell_name}'
    pot_file = 'gap_files/Si.ZBL-stiff.TGAP.gap'
    n_species = 1
    species = Si
    masses = 28.09   
    
    md_nsteps = {md_nsteps}
    md_step = 1.
    
    t_beg = {temp}
    t_end = {temp}
    tau_t = 100.
    thermostat = bussi 
    
    p_beg = 1
    p_end = 1
    tau_p = 200.
    gamma_p = 40 !B_Si/B_water
    barostat = berendsen
    barostat_sym = diag
    
    write_xyz = 200
    write_thermo = 1
    write_lv = .true.
    """
    f = open('input', 'w')
    f.write(input_str)
    f.close()


#---------- Controller variables 1 -----------------#
# Number of MD steps for equilibrating the pristine cell:
md_nsteps_eq = 5

# Equilibration temperature (K) of the pristine cell:
temp_eq = 30 
#------------------------------------------------------

# Now, let's run cell equilibration:
create_tgap_input_eq(pcell, temp_eq, md_nsteps_eq)
run_turbogap()


# Check how the temperature and pressure vary:
steps, T, epot, P = np.loadtxt('thermo.log', usecols=(0,2,4,5), unpack=True)
fig, axs = plt.subplots(1, 3, figsize=(12,4), sharex=True)
axs[0].plot(steps, T)
axs[0].set_ylabel("Temperature (K)")
axs[1].plot(steps, P)
axs[1].set_ylabel("Pressure (bar)")
axs[2].plot(steps, epot)
axs[2].set_ylabel("Potential energy (eV)")
fig.supxlabel("Steps")
plt.tight_layout()
plt.show()


# In[ ]:


# to run the TDE simulation, the following function will be used.

def calc_velocity(E, direction, element):
    """
    Calculates velocity components (Ang/ps) to be assigned to the PKA atom

    Parameters:
        E:          kinetic energy of PKA (eV)
        direction:  [h,k,l]
        element:    symbol of the element (e.g 'Si')

    Returns:
        Velocity components: (Vx, Vy, Vz) in [Ang/ps]
    
    """
    m = {'Si':28.0855, 'C':12.011, 'Ge':72.64}
    #
    Vtot = np.sqrt((2.0 * 1.60218*10**8 * E) / (m[element] * 1.66054)) / 100.0
    # 
    vec = np.asarray(direction, dtype=float)
    norm = np.linalg.norm(vec)
    unit_vec = vec / norm
    #
    Vx = Vtot * unit_vec[0] 
    Vy = Vtot * unit_vec[1]
    Vz = Vtot * unit_vec[2]
    #
    return Vx, Vy, Vz


#---------- Controller variables 2 -----------------#
# TDE dir:
tde_dir = [2, 4, 3]

# The energy of the PKA atom (eV):
E_pka = 20 

# The index of the PKA atom in the pristine cell:
PKA_indx = 104
#------------------------------------------------------

# Velocity components:
Vx, Vy, Vz = calc_velocity(E_pka, tde_dir, 'Si') 

# The last frame of the equilibrated trajectory is taken to perform TDE calculation:
atoms_eq = read('trajectory_out.xyz', index='-1')

# Setting the velocity vector for the PKA atom here.
atoms_pka = atoms_eq.copy()
atoms_pka.arrays['velocities'][PKA_indx] = np.array([vx, vy, vz]) / 1000 #Ang/fs

# And exporting the cell to be read by TurboGAP:
cell_tde = 'tde.xyz'
write(cell_tde, atoms_pka)


# In[ ]:


# We are set to launch the PKA and check the defect generation:

def create_tgap_input_tde(cell_name, md_nsteps):
    """
    Creates TurboGAP input file to run TDE simulation.

    Parameters:
        cell_name : structure file in xyz format
        md_nsteps : number of steps
    
    Returns:
        The 'input' file is written in the directory

    """
    input_str = f"""! Species-specific info
    atoms_file = '{cell_name}'
    pot_file = 'gap_files/Si.ZBL-stiff.TGAP.gap'
    n_species = 1
    species = Si
    masses = 28.09   

    md_nsteps = {md_nsteps}

    write_thermo = 1
    write_xyz = 2

    adaptive_time = .true.
    !adapt_time_groupID = all
    adapt_tstep_interval = 1
    adapt_tmin = 1.0E-10
    adapt_tmax = 3.0E-00
    adapt_xmax = 1.0E-01
    adapt_emax = 30.0
    """
    f = open('input', 'w')
    f.write(input_str)
    f.close()


#---------- Controller variables 4 -----------------#
# Number of MD steps in TDE simulations:
md_nsteps_tde = 300
#------------------------------------------------------

create_tgap_input_tde(cell_tde, md_nsteps_tde)
run_turbogap()


# In[ ]:


# Let's visually check if the defect is generated. If not, 
# we should increase the PKA energy and with an specific 
# interval, 1 or 2 eV?

# Please continue increasing the energy, until you find an 
# stable defect!

traj = read('trajectory_out.xyz', index=':')
viewer = visualize(traj); viewer


### Introduction

In this tutorial, we run a low-energy PKA cascade simulation to explore defect generation through atomic displacements. Starting from a basic input with a constant timestep, we progressively incorporate recently implemented modules in the TurboGAP code (https://doi.org/10.1016/j.commatsci.2026.114560) that are relevant to cascade dynamics. Specifically, we examine **adaptive timestep calculation** and the inclusion of **electronic stopping** to more accurately capture the high-energy dynamics of the cascade.


### Implementation details

In this tutorial, we implement the TDE calculation through a Python workflow. 

The implementation follows three main phases:

* **Phase 1: Cell Equilibration** We begin by thermalizing Silicon supercell at a target temperature. This ensures the lattice contains realistic thermal displacements and velocities before the impact event occurs.
    
* **Phase 2: PKA Selection and Velocity Initialization** A specific atom is designated as the **PKA**. Based on the chosen crystallographic direction, we calculate the velocity components $(v_x, v_y, v_z)$ required to match the target PKA energy in electronvolts (eV).
    
* **Phase 3: MD Execution and Defect Analysis** The dynamics are launched. After the simulation, we visually check the trajectory to determine if a stable defect has been created. If no defect is found, the simulation should be run with the $E+\Delta E$ PKA energy.


author: Tigany Zarrouk
title: Simulations With Experimental Observables

# Introduction

In this tutorial, we will go through the more unique features of the
TurboGAP code that set it apart from other machine-learning interatomic
potential codes/engines: the ability to predict experimental
observables, and infer structures from experimental data via multiple
means.

TurboGAP can give predictions which scale linearly with the number of
atoms for:

1.  X-ray diffraction (XRD)
2.  Neutron diffraction (ND)
3.  Pair Distribution Functions (PDFs) - both standard and corrected by
    atomic form factors/neutron scattering lengths.
4.  X-ray Photoelectron Spectroscopy (XPS)

And we further have aims to extend this to more observables: Raman, IR,
NMR, XAS and TEM just to name a few!

In this tutorial, we will try to be detectives: given some experimental
data, and knowledge of the species proportions, can we find out what is
the most likey structure that makes sense?

First, lets see how we can make an experimental observable prediction.

# Prediction

# Structural Inference

## Reverse Monte-Carlo

### Theory of Generalized-Hamiltonian GCMC

As seen in our paper *Experiment-Driven Atomistic Materials Modeling: A
Case Study Combining X-Ray Photoelectron Spectroscopy and Machine
Learning Potentials to Infer the Structure of Oxygen-Rich Amorphous
Carbon* <https://pubs.acs.org/doi/full/10.1021/jacs.4c01897>

We can create an XPS-optimized structure by modifying the total energy
of the system $E_{\rm total}$ with a pseudoenergy term $E_{\rm spectra}$
which reflects how well our predicted spectra
$g_{\rm pred}(E, \{\mathbf{r}\})$ agrees with an experimental spectra
$g_{\rm exp}(E)$, where here $E$ corresponds to the core-electron
binding energy scale. $$ \tilde{E} = E_{\rm total} + E_{\rm spectra} $$

We define
$$ E_{\rm spectra} = \frac{1}{2} \gamma \left( \mathbf{g}_{\rm pred} - \mathbf{g}_{\rm pred} \right)^2$$
where the bold font shows that we have represented the spectrum as a
vector, with samples $[\mathbf{g}]_i$ at $[\mathbf{E}]_i$.

We can use this energy Grand-Canonical Monte-Carlo simulations to create
structures which agree with experimental XPS data by design.

### Invoking XPS optimization in Turbogap

We simply add this to the input file

``` conf
# Experimental Data Specification
n_exp = 1                                     # Number of experimental observables we wish to recreate
exp_labels = 'xps'                            # Labels of experimental observables (currently limited to xps/xrd/nd/pdf)
exp_data_files = 'xps_spectra_interp.dat'     # Experimental data
exp_n_samples = 501                           # Number of samples for linear interpolation of experimental data (needed if data is not on a uniform grid), this number should be greater than the number of data points in the experimental file.
exp_energy_scales = 10.0                      # The energy scale "gamma" as above
```

If experimental data is added, and it is possible to calculate the
observable, **TurboGAP** by default will calculate the $E_{\rm spectra}$
term and add it to the total energy.

To turn this off, we can set \`exp~energies~ = .false.\`

We can also do reverse monte-carlo using multiple types of experimental
data, such as with this arbitrary example.

``` conf
# Experimental Data Specification
n_exp = 2                                     # Number of experimental observables we wish to recreate
exp_labels = 'xps' 'xrd'                            # Labels of experimental observables (currently limited to xps/xrd/nd/pdf)
exp_data_files = 'xps_spectra_interp.dat' 'xrd_CO.dat'     # Experimental data
exp_n_samples = 501 201                           # Number of samples for linear interpolation of experimental data (needed if data is not on a uniform grid), this number should be greater than the number of data points in the experimental file.
exp_energy_scales = 10.0 100.0                     # The energy scale "gamma" as above
```

## Molecular Augmented Dynamics

Reverse Monte-Carlo, despite it being

Molecular Augmented Dynamics is an MD-driven means to infer the
structure.

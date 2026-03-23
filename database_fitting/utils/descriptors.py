from quippy.descriptors import Descriptor 
from ase.io import read, write
import numpy as np

def make_soap_descriptor(atom_sigma=0.5, cutoff=3.0, l_max=4, n_max=4):
    soap_str = (
        f"soap cutoff={cutoff} "
        f"l_max={l_max} "
        f"n_max={n_max} "
        f"atom_sigma={atom_sigma} "
        f"n_Z=1 Z1=6"
    )
    return Descriptor(soap_str)

def build_atomic_dataset(structures, descriptor):
    X_all = []
    e_all = []

    for atoms in structures:
        E_total = atoms.get_potential_energy()

        desc = descriptor.calc(atoms, descriptor_only=True)
        X_atoms = desc["data"]

        E_per_atom = E_total / len(atoms)
        e_atoms = np.full(len(atoms), E_per_atom)

        X_all.append(X_atoms)
        e_all.append(e_atoms)

    X = np.vstack(X_all)
    e = np.concatenate(e_all)

    return X, e
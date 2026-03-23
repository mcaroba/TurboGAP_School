from quippy.descriptors import Descriptor 
import numpy as np
from .kernel import soap_kernel_matrix



def predict_structure_energy(atoms, descriptor, X_train, alpha, zeta=4):
    desc = descriptor.calc(atoms, descriptor_only=True)
    X_test = desc["data"]

    K_test = soap_kernel_matrix(X_test, X_train, zeta=zeta)
    local_energies = K_test @ alpha

    return np.sum(local_energies)

def predict_dataset(structures, descriptor, X_train, alpha, zeta=4):
    E_pred_total = [predict_structure_energy(a, descriptor, X_train, alpha, zeta=zeta)
                    for a in structures]
    E_pred_atom = [E_pred_total[i] / len(structures[i]) for i in range(len(structures))]
    E_true_atom = [a.get_potential_energy() / len(a) for a in structures]

    return np.array(E_true_atom), np.array(E_pred_atom)
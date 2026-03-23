import numpy as np


def soap_kernel_matrix(X1, X2, zeta=4):
    K = np.dot(X1, X2.T)
    return K ** zeta
    
def train_gap_like_model(X_train, e_train, sigma_n=1e-2, zeta=4):
    K = soap_kernel_matrix(X_train, X_train, zeta=zeta)
    K += sigma_n**2 * np.eye(len(X_train))

    L = np.linalg.cholesky(K)
    y1 = np.linalg.solve(L, e_train)
    alpha = np.linalg.solve(L.T, y1)

    return alpha, K, L
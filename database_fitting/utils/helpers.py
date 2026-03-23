from sklearn.metrics import r2_score, mean_squared_error
from ase.io import read, write
import os
import random
import numpy as np
import matplotlib.pyplot as plt

def split_xyz(input_file, test_size=0.2, seed=42):

    structures = read(input_file, index=":")
    print(f"Loaded {len(structures)} structures from {input_file}")

    random.seed(seed)
    random.shuffle(structures)

    split_idx = int(len(structures) * (1 - test_size))
    train_structures = structures[:split_idx]
    test_structures = structures[split_idx:]

    input_name = os.path.basename(input_file).split('.')[0]

    train_file = f"{input_name}_train.xyz"
    test_file = f"{input_name}_test.xyz"

    write(train_file, train_structures)
    write(test_file, test_structures)

    print(f"Split complete: {len(train_structures)} train, {len(test_structures)} test")

    return train_file, test_file

def parity_plot(y_true, y_pred, title="Parity plot"):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    r2 = r2_score(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))

    plt.figure(figsize=(6, 6))
    plt.scatter(y_true, y_pred, s=20, alpha=0.7)
    plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], "k--")
    plt.xlabel("DFT energy / atom (eV)")
    plt.ylabel("Predicted energy / atom (eV)")
    plt.title(title)
    plt.text(
        0.05, 0.95,
        f"R² = {r2:.3f}\nRMSE = {rmse:.4f} eV",
        transform=plt.gca().transAxes,
        va="top",
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.8)
    )
    plt.tight_layout()
    plt.show()
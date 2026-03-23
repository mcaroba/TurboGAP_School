from ase.io import read
from collections import defaultdict
import sys

iter_name = sys.argv[1]

ref_file = "CHgap.xyz"
gap_file = "iter_md.xyz"

ref_atoms = read(ref_file, ":")
gap_atoms = read(gap_file, ":")

assert len(ref_atoms) == len(gap_atoms), "Files must have same number of structures!"

data = defaultdict(list)

for ref, gap in zip(ref_atoms, gap_atoms):
    n = len(ref)

    ref_energy = ref.info.get("energy", ref.get_potential_energy())
    gap_energy = gap.info.get("energy", gap.get_potential_energy())
    data[n].append(f"{n} {ref_energy:.8f} {gap_energy:.8f}\n")


with open(f"e_{iter_name}.dat", "w") as f:
    for n in sorted(data):
        f.writelines(data[n])
print(f"Written e_{iter_name}.dat")
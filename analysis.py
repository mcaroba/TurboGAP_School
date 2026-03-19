"""
Analyse and plot hydrogen adsorption on a PdAu nanoparticle.
Coordination-based site classification — works for any nanoparticle shape.
"""

import re
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from collections import Counter, defaultdict
from ase.io import read
from ase.neighborlist import NeighborList

# -----------------------------------------------------------------------
# HELPER
# -----------------------------------------------------------------------
def normalize_comp(comp):
    return ''.join(sorted(re.findall(r'[A-Z][a-z]?', comp)))

def comp_color(c):
    elems = re.findall(r'[A-Z][a-z]?', c)
    if all(e == 'Pd' for e in elems):
        return 'steelblue'
    if all(e == 'Au' for e in elems):
        return 'goldenrod'
    return 'mediumseagreen'

print(f"Working directory: {os.getcwd()}")

# -----------------------------------------------------------------------
# 1. LOAD STRUCTURE
# -----------------------------------------------------------------------
atoms = read('mc_current.xyz')
atoms.pbc = False

syms     = atoms.get_chemical_symbols()
n_atoms  = len(atoms)
h_idx    = [i for i, s in enumerate(syms) if s == 'H']
pd_idx   = [i for i, s in enumerate(syms) if s == 'Pd']
au_idx   = [i for i, s in enumerate(syms) if s == 'Au']
metal_idx = pd_idx + au_idx

print(f"Pd atoms : {len(pd_idx)}")
print(f"Au atoms : {len(au_idx)}")
print(f"H atoms  : {len(h_idx)}")

# -----------------------------------------------------------------------
# 2. BUILD NEIGHBOR LIST
# -----------------------------------------------------------------------
cutoff_H_metal  = 2.5   # H-metal bond cutoff (Angstrom)
cutoff_metal    = 3.5   # metal-metal cutoff for coordination number

# use max cutoff for the neighbor list
nl = NeighborList(
    [max(cutoff_H_metal, cutoff_metal) / 2] * n_atoms,
    self_interaction=False,
    bothways=True,
)
nl.update(atoms)

# -----------------------------------------------------------------------
# 3. COORDINATION NUMBER — identify surface vs bulk metal atoms
# -----------------------------------------------------------------------
coord_numbers = np.zeros(n_atoms, dtype=int)
for i in metal_idx:
    neighbors, _ = nl.get_neighbors(i)
    # count only metal neighbors within metal cutoff
    metal_neigh = [n for n in neighbors
                   if syms[n] in ('Pd', 'Au')
                   and np.linalg.norm(atoms.positions[i] -
                                      atoms.positions[n]) < cutoff_metal]
    coord_numbers[i] = len(metal_neigh)

surf_idx = [i for i in metal_idx if coord_numbers[i] < 11]
bulk_idx = [i for i in metal_idx if coord_numbers[i] >= 11]

print(f"\nSurface metal atoms : {len(surf_idx)}")
print(f"Bulk metal atoms    : {len(bulk_idx)}")
print(f"Mean CN surface     : {np.mean([coord_numbers[i] for i in surf_idx]):.2f}")
print(f"Mean CN bulk        : {np.mean([coord_numbers[i] for i in bulk_idx]):.2f}")

# CN distribution
cn_counter = Counter(coord_numbers[i] for i in metal_idx)
print("\nCN distribution (metal atoms):")
for cn, count in sorted(cn_counter.items()):
    print(f"  CN={cn:2d}: {count}")

# -----------------------------------------------------------------------
# 4. CLASSIFY H ATOMS BY LOCAL COORDINATION
# -----------------------------------------------------------------------
site_data = []

for hi in h_idx:
    neighbors, _ = nl.get_neighbors(hi)

    # metal neighbors within H-metal cutoff
    metal_neigh = [n for n in neighbors
                   if syms[n] in ('Pd', 'Au')
                   and np.linalg.norm(atoms.positions[hi] -
                                      atoms.positions[n]) < cutoff_H_metal]
    n_metal = len(metal_neigh)
    comp_counter = Counter(syms[n] for n in metal_neigh)
    comp_str = ''.join(sorted([syms[n] for n in metal_neigh]))

    # site classification by number of metal neighbors
    if n_metal == 0:
        site = 'unbound'
    elif n_metal == 1:
        site = 'ontop'
    elif n_metal == 2:
        site = 'bridge'
    elif n_metal == 3:
        site = 'hollow3'
    elif n_metal == 4:
        site = 'hollow4'
    else:
        site = 'subsurface'

    # check if H is subsurface: all metal neighbors are bulk atoms
    if n_metal > 0 and all(coord_numbers[n] >= 11 for n in metal_neigh):
        site = 'subsurface'

    # bond lengths to each metal neighbor
    bond_lengths = [np.linalg.norm(atoms.positions[hi] -
                                   atoms.positions[n])
                    for n in metal_neigh]
    mean_bond = np.mean(bond_lengths) if bond_lengths else 0.0

    site_data.append({
        'h_index':   hi,
        'site':      site,
        'n_metal':   n_metal,
        'n_Pd':      comp_counter.get('Pd', 0),
        'n_Au':      comp_counter.get('Au', 0),
        'comp':      normalize_comp(comp_str) if comp_str else 'none',
        'mean_bond': mean_bond,
        'position':  atoms.positions[hi],
    })

# -----------------------------------------------------------------------
# 5. PRINT SUMMARY
# -----------------------------------------------------------------------
by_site = Counter(d['site'] for d in site_data)
by_comp = Counter(d['comp'] for d in site_data)

print(f"\n--- H site classification (coordination-based) ---")
for k, v in sorted(by_site.items()):
    print(f"  {k:15s}: {v}")

print(f"\n--- H site compositions ---")
for k, v in sorted(by_comp.items()):
    print(f"  {k:20s}: {v}")

print(f"\nMean metal neighbors per H : "
      f"{np.mean([d['n_metal'] for d in site_data]):.2f}")
print(f"Mean Pd neighbors per H    : "
      f"{np.mean([d['n_Pd'] for d in site_data]):.2f}")
print(f"Mean Au neighbors per H    : "
      f"{np.mean([d['n_Au'] for d in site_data]):.2f}")
print(f"Mean H-metal bond length   : "
      f"{np.mean([d['mean_bond'] for d in site_data if d['mean_bond'] > 0]):.3f} Å")

# -----------------------------------------------------------------------
# 6. PLOT 1 — bar charts: site type and composition
# -----------------------------------------------------------------------
site_colors_map = {
    'ontop':      'orchid',
    'bridge':     'coral',
    'hollow3':    'steelblue',
    'hollow4':    'goldenrod',
    'subsurface': 'gray',
    'unbound':    'black',
}

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# site type
ax = axes[0]
sites  = sorted(by_site.keys())
counts = [by_site[s] for s in sites]
colors = [site_colors_map.get(s, 'gray') for s in sites]
bars   = ax.bar(sites, counts, color=colors, alpha=0.85, edgecolor='white')
ax.bar_label(bars, fontsize=10)
ax.set_ylabel('Number of H atoms')
ax.set_title('H site types (coordination-based)')
ax.set_xticklabels(sites, rotation=30, ha='right')
patches = [mpatches.Patch(color=c, label=s)
           for s, c in site_colors_map.items() if s in by_site]
ax.legend(handles=patches, fontsize=8)

# composition
ax = axes[1]
comps  = sorted(by_comp.keys())
counts = [by_comp[c] for c in comps]
colors = [comp_color(c) for c in comps]
bars   = ax.bar(comps, counts, color=colors, alpha=0.85, edgecolor='white')
ax.bar_label(bars, fontsize=10)
ax.set_ylabel('Number of H atoms')
ax.set_title('H site compositions')
ax.set_xticks(range(len(comps)))
ax.set_xticklabels(comps, rotation=30, ha='right')
patches = [
    mpatches.Patch(color='steelblue',     label='pure Pd'),
    mpatches.Patch(color='mediumseagreen', label='mixed PdAu'),
    mpatches.Patch(color='goldenrod',      label='pure Au'),
]
ax.legend(handles=patches, fontsize=8)

plt.suptitle('H adsorption on PdAu nanoparticle', fontsize=13)
plt.tight_layout()
plt.savefig('site_analysis.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved: site_analysis.png")

# -----------------------------------------------------------------------
# 7. PLOT 2 — heatmap: site type vs composition
# -----------------------------------------------------------------------
sites_list = sorted(set(d['site'] for d in site_data))
comps_list = sorted(set(d['comp'] for d in site_data))

mat = np.zeros((len(sites_list), len(comps_list)), dtype=int)
for d in site_data:
    if d['site'] in sites_list and d['comp'] in comps_list:
        mat[sites_list.index(d['site'])][comps_list.index(d['comp'])] += 1

fig, ax = plt.subplots(figsize=(10, 5))
im = ax.imshow(mat, cmap='Blues', aspect='auto')
ax.set_xticks(range(len(comps_list)))
ax.set_yticks(range(len(sites_list)))
ax.set_xticklabels(comps_list, rotation=30, ha='right', fontsize=10)
ax.set_yticklabels(sites_list, fontsize=10)
ax.set_xlabel('Composition')
ax.set_ylabel('Site type')
ax.set_title('H site type vs composition — PdAu nanoparticle')
for i in range(len(sites_list)):
    for j in range(len(comps_list)):
        if mat[i, j] > 0:
            ax.text(j, i, str(mat[i, j]),
                    ha='center', va='center', fontsize=10,
                    color='white' if mat[i, j] > mat.max() * 0.5 else 'black')
plt.colorbar(im, ax=ax, label='count')
plt.tight_layout()
plt.savefig('heatmap_site_comp.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved: heatmap_site_comp.png")

# -----------------------------------------------------------------------
# 8. PLOT 4 — coordination number distribution of metal atoms
# -----------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# CN distribution for Pd vs Au
ax = axes[0]
for elem, idx_list, color in [('Pd', pd_idx, 'steelblue'),
                                ('Au', au_idx, 'goldenrod')]:
    cns = [coord_numbers[i] for i in idx_list]
    if cns:
        cn_vals = sorted(set(cns))
        counts  = [cns.count(c) for c in cn_vals]
        ax.plot(cn_vals, counts, 'o-', color=color,
                label=elem, linewidth=2, markersize=6)
ax.axvline(11, color='red', linestyle='--', linewidth=1,
           label='surface/bulk threshold (CN=11)')
ax.set_xlabel('Coordination number')
ax.set_ylabel('Count')
ax.set_title('CN distribution: Pd vs Au')
ax.legend()

# CN of metal atoms bonded to H
ax = axes[1]
h_bonded_cn = []
h_bonded_elem = []
for d in site_data:
    hi = d['h_index']
    neighbors, _ = nl.get_neighbors(hi)
    metal_neigh = [n for n in neighbors
                   if syms[n] in ('Pd', 'Au')
                   and np.linalg.norm(atoms.positions[hi] -
                                      atoms.positions[n]) < cutoff_H_metal]
    for n in metal_neigh:
        h_bonded_cn.append(coord_numbers[n])
        h_bonded_elem.append(syms[n])

for elem, color in [('Pd', 'steelblue'), ('Au', 'goldenrod')]:
    cns = [cn for cn, el in zip(h_bonded_cn, h_bonded_elem) if el == elem]
    if cns:
        cn_vals = sorted(set(cns))
        counts  = [cns.count(c) for c in cn_vals]
        ax.plot(cn_vals, counts, 'o-', color=color,
                label=elem, linewidth=2, markersize=6)
ax.axvline(11, color='red', linestyle='--', linewidth=1,
           label='surface/bulk threshold (CN=11)')
ax.set_xlabel('Coordination number of metal atom bonded to H')
ax.set_ylabel('Count')
ax.set_title('CN of metal atoms bonded to H')
ax.legend()

plt.suptitle('Coordination numbers — PdAu nanoparticle', fontsize=13)
plt.tight_layout()
plt.savefig('coordination.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved: coordination.png")

# -----------------------------------------------------------------------
# 9. WRITE OVITO XYZ WITH SITE TYPE COLUMN
# -----------------------------------------------------------------------
site_label = {
    'ontop':      1,
    'bridge':     2,
    'hollow3':    3,
    'hollow4':    4,
    'subsurface': 5,
    'unbound':    6,
}

h_site_type = {d['h_index']: site_label.get(d['site'], 0)
               for d in site_data}

with open('mc_current.xyz', 'r') as f:
    lines = f.readlines()

n_file    = int(lines[0].strip())
comment   = lines[1].strip()
datalines = lines[2:2 + n_file]

site_type_col = np.zeros(n_file, dtype=int)
for i, atom in enumerate(atoms):
    if atom.symbol == 'H':
        site_type_col[i] = h_site_type.get(i, 0)

with open('nanoparticle_H_colored.xyz', 'w') as f:
    f.write(f"{n_file}\n")
    f.write(f"{comment} "
            f"site_type=0:metal,1:ontop,2:bridge,3:hollow3,4:hollow4,"
            f"5:subsurface,6:unbound\n")
    for i, line in enumerate(datalines):
        f.write(f"{line.rstrip()} {site_type_col[i]}\n")

print("Saved: nanoparticle_H_colored.xyz")
print("\nDone. Figures: site_analysis.png, heatmap_site_comp.png, "
      "bond_lengths.png, coordination.png")
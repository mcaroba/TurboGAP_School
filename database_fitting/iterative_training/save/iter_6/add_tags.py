# HND XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# HND X
# HND X   TurboGAP
# HND X
# HND X   TurboGAP is copyright (c) 2019-2021, Miguel A. Caro and others
# HND X
# HND X   TurboGAP is published and distributed under the
# HND X      Academic Software License v1.0 (ASL)
# HND X
# HND X   This file, add_tags.py, is copyright (c) 2019-2021, Miguel A. Caro
# HND X
# HND X   TurboGAP is distributed in the hope that it will be useful for non-commercial
# HND X   academic research, but WITHOUT ANY WARRANTY; without even the implied
# HND X   warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# HND X   ASL for more details.
# HND X
# HND X   You should have received a copy of the ASL along with this program
# HND X   (e.g. in a LICENSE.md file); if not, you can write to the original
# HND X   licensor, Miguel Caro (mcaroba@gmail.com). The ASL is also published at
# HND X   http://github.com/gabor1/ASL
# HND X
# HND X   When using this software, please cite the following reference:
# HND X
# HND X   Miguel A. Caro. Phys. Rev. B 100, 024112 (2019)
# HND X
# HND XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

from ase.io import read, write
import numpy as np
import sys

#############################################################################################
# User modifiable values:

# Input/output filenames
input_database ="train.xyz"
output_database = "train_tagged.xyz"

virial_only = True
custom_code = True

# Energy and virial regularization options. All values in eV/atom! The code will adjust for
# the total number of atoms in each configuration. sigma_e is a dictionary. The code will
# look in your input XYZ file for a config_type tag. You need to provide the list of config
# types for which you want to add custom regularization to the dictionary. If it can't find a
# config type in the dictionary (or no config type at all), it will use the "default" value.
# So "default" *needs* to be an entry in the dictionary. sigma_e and sigma_v do not
# necessarily need to contain all (or the same) config types, only those for which you want
# to add specific regularization other than the default ones.

sigma_e = {
    "default": 0.001,
    "iter_1": 0.025,
    "iter_2": 0.024,
    "iter_3": 0.023,
    "iter_4": 0.022,
    "iter_5": 0.021,
    "iter_6": 0.020,
    "iter_7": 0.019,
    "iter_8": 0.018,
    "iter_9": 0.017,
    "iter_10": 0.016,
    "iter_11": 0.015,
    "iter_12": 0.014,
    "iter_13": 0.013,
    "iter_14": 0.012,
    "iter_15": 0.011,
    "iter_16": 0.010,
    "iter_17": 0.009,
    "iter_18": 0.008,
    "iter_19": 0.007,
    "iter_20": 0.006,}
print("Reading database...")
at = read(input_database, index=":")
print("")
print("... done.")
print("Adding energy reg. param.")
# The structures are looped in reversed order so that the user can safely remove them using custom code
for i in reversed(range(0, len(at))):
#   Bookkeeping
    at[i].pbc = True
    vol = at[i].get_volume()
    if "config_type" in at[i].info:
        ct = at[i].info["config_type"]
    else:
        ct = "default"
#   Energy  part
    n = len(at[i])
    if ct in sigma_e:
        se = np.sqrt(n) * sigma_e[ct]
    else:
        se = np.sqrt(n) * sigma_e["default"]
    at[i].info["energy_sigma"] = se


#   Print progress
    sys.stdout.write('\rProgress:%6.1f%%' % ((len(at)-float(i))*100./float(len(at))) )
    sys.stdout.flush()
print("")
print("")

print("Writing to file...")
write(output_database, at)
print("")
print("... done.")

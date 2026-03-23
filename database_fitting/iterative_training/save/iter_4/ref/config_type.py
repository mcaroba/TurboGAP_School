from ase.io import read, write
import sys

source = read("iter_md.xyz", ":")
target = read("trajectory_out.xyz", ":")

config = sys.argv[1]

assert len(source) == len(target), "Mismatch in number of structures"

for s, t in zip(source, target):
    s.info["config_type"] = config
    t.info["config_type"] = config

write("CHgap.xyz", target)
write("turbogap.xyz", source)

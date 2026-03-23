#!/usr/bin/env bash

name=$1

echo "=== MD iteration ${name} ==="

mkdir -p iterations/iter_${name}/turbogap
cp -r  iterations/iter_${name}/runs/iter_${name}/gap_files/ iterations/iter_${name}/turbogap/gap_files/

cd iterations/iter_${name}/turbogap

cp -r ../../../inputs/mds/* .

python3 make_initial.py

cp melt input
mpirun -np 3 turbogap md

n=$(head -1 trajectory_out.xyz | awk '{print $1+2}')
tail -${n} trajectory_out.xyz > melt.xyz

cp quench input
mpirun -np 3 turbogap md

cp trajectory_out.xyz iter_md.xyz

cd ../../..

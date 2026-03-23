#!/usr/bin/env bash

name=$1

echo "=== Recompute reference data from iteration ${name} with our "ground truth" ==="

mkdir -p iterations/iter_${name}/ref
cd iterations/iter_${name}/ref

#cp -r ../../inputs/ref_inits/* .
cp ../../../inputs/ref_inits/* .
ln -sfn ../../../inputs/ref_inits/gap_files gap_files

cp ../turbogap/iter_md.xyz .

mpirun -np 3 turbogap predict

python3 config_type.py iter_${name}
python3 extract_energies.py iter_${name}

cd ../../..

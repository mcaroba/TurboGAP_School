#!/usr/bin/env bash

name=$1
prev=$((name - 1))

echo "=== PREPARE iteration ${name} ==="

mkdir -p iterations/iter_${name}
cd iterations/iter_${name}

cp ../../inputs/fits/* .

cp ../iter_${prev}/train.xyz prev_db.xyz
cp ../iter_${prev}/ref/CHgap.xyz .
cat prev_db.xyz CHgap.xyz > train.xyz

python3 add_tags.py

cd ../../

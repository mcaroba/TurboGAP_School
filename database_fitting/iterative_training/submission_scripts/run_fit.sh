#!/usr/bin/env bash

name=$1

echo "=== FIT iteration ${name} ==="

mkdir -p iterations/iter_${name}/runs/iter_${name}
cd iterations/iter_${name}/runs/iter_${name}

ln -sf ../../pairpot_mod.xml
ln -sf ../../train_tagged.xyz train_tagged.xyz

cp ../../soap_turbo.sh .

bash ./soap_turbo.sh

pip install lxml # environment doesn't have this, an easy fix

python3 /home/jovyan/shared/apps/turbogap/turbogap_2026-02-25/tools/quip_xml_to_gap/make_gap_files.py CH.xml CH.gap

cd ../../../..


# Analysis and Visualization of Simulation Results
---

In this tutorial, we have:

- Demo 1 -- introduction to different dimensionality reduction techniques

- Demo 2 -- analysis and visualization of results, in particular: 
	- understanding the practicalities of clustering and embedding through cl-MDS
	- visualizing SOAP kernels
	- including relevant simulation information: local energies, Hirschfeld volumes, sparsification

### During TurboGAP school

[HackMD document for collaborative learning](https://hackmd.io/o_Syx0ZDTee5dnpgfoj5gA#Analysis-and-Data-Visualization)

Everything else is ready on the Noppe virtual environment, you are good to go!


### After TurboGAP school

Create the virtual environment using 
```
python3 -m env-name .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

Without deactivating the Python venv, follow [cl-MDS repository](https://github.com/mcaroba/cl-MDS/tree/master) 
installation instructions as shown below:
```
git clone --recursive http://github.com/mcaroba/cl-MDS.git
chmod +x build_libraries.sh
./build_libraries.sh
echo "export PYTHONPATH=$(pwd):\$PYTHONPATH" >> ~/.bashrc
echo "export PYTHONPATH=$(pwd)/ase_tools:\$PYTHONPATH" >> ~/.bashrc
source ~/.bashrc
```

Happy embedding! :)

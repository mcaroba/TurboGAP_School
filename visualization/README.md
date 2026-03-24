
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


## References

**Demo 1*

- CHO database: 
	- *Accurate Computational Prediction of Core-Electron Binding Energies in Carbon-Based Materials: A Machine-Learning Model Combining Density-Functional Theory and GW*,
[Chem. Mater. 2022, 34, 14, 6240–6254](https://pubs.acs.org/doi/10.1021/acs.chemmater.1c04279)

- Comparison of dimensionality reduction techniques:
	- Scikit-learn documentation on [*Manifold learning*](https://scikit-learn.org/stable/modules/manifold.html)
	- *Cluster-based multidimensional scaling embedding tool for data visualization*, 
[P. Hernández-León, M. A. Caro, 2024 Phys. Scr. 99 066004](https://iopscience.iop.org/article/10.1088/1402-4896/ad432e)
	- *UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction*,
[L. McInnes, J. Healy, J. Melville, 2020 arXiv:1802.03426v3](https://arxiv.org/abs/1802.03426)


**Demo 2**

- GST database:
	- *Modeling the Phase-Change Memory Material, Ge2Sb2Te5, with a Machine-Learned Interatomic Potential*,
[F. C. Mocanu, K. Konstantinou, et al., J. Phys. Chem. B 2018, 122, 38, 8998–9006](https://pubs.acs.org/doi/10.1021/acs.jpcb.8b06476)

- Cluster MDS:
	- [cl-MDS repository](https://github.com/mcaroba/cl-MDS)
	- *Cluster-based multidimensional scaling embedding tool for data visualization*, 
[P. Hernández-León, M. A. Caro, 2024 Phys. Scr. 99 066004](https://iopscience.iop.org/article/10.1088/1402-4896/ad432e)

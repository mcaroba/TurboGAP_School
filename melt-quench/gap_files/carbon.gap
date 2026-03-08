gap_beg distance_2b
species1 = C
species2 = C
delta = 0.5
sigma = 0.5
rcut = 3.7
desc_sparse = 'gap_files/carbon.xml.sparseX.GAP_2021_7_24_180_11_46_46_951'
alphas_sparse = 'gap_files/alphas_2b_1.dat'
gap_end

gap_beg angle_3b
species_center = C
species1 = C
species2 = C
delta = 0.003
sigma = 4.0 4.0 4.0
kernel_type = "pol"
rcut = 3.0
desc_sparse = 'gap_files/carbon.xml.sparseX.GAP_2021_7_24_180_11_46_46_952'
alphas_sparse = 'gap_files/alphas_3b_1.dat'
gap_end

gap_beg soap_turbo
n_species = 1
species = C
central_species = 1
rcut = 3.7 
buffer = 0.5 
atom_sigma_r = 0.5 
atom_sigma_t = 0.5 
atom_sigma_r_scaling = 0 
atom_sigma_t_scaling = 0 
amplitude_scaling = 1.0 
n_max = 8 
l_max = 8
nf = 4 
central_weight = 1.0 
scaling mode = polynomial
basis = "poly3gauss"
radial_enhancement = 1
zeta = 6
delta = 0.1
desc_sparse = 'gap_files/carbon.xml.sparseX.GAP_2021_7_24_180_11_46_46_953'
alphas_sparse = 'gap_files/alphas_mb_1.dat'
compress_soap = .true.
file_compress_soap = 'gap_files/compress_1.dat'
gap_end

gap_beg core_pot
species1 = C
species2 = C
core_pot_file = 'gap_files/core_pot_1.dat'
gap_end core_pot


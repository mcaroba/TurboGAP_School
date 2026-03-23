gap_beg distance_2b
species1 =  H
species2 =  H
delta = 0.5
sigma = 0.5
rcut = 4.0
desc_sparse = "gap_files/CH.xml.sparseX.GAP_2026_3_23_120_0_19_4_471"
alphas_sparse = "gap_files/alphas_distance_2b_1.dat"
gap_end

gap_beg distance_2b
species1 =  H
species2 = C
delta = 0.5
sigma = 0.5
rcut = 4.0
desc_sparse = "gap_files/CH.xml.sparseX.GAP_2026_3_23_120_0_19_4_472"
alphas_sparse = "gap_files/alphas_distance_2b_2.dat"
gap_end

gap_beg distance_2b
species1 = C
species2 = C
delta = 0.5
sigma = 0.5
rcut = 4.0
desc_sparse = "gap_files/CH.xml.sparseX.GAP_2026_3_23_120_0_19_4_473"
alphas_sparse = "gap_files/alphas_distance_2b_3.dat"
gap_end

gap_beg angle_3b
species_center = C
species1 =  H
species2 =  H
delta = 0.01
sigma = 0.20000000000000000E+001  0.20000000000000000E+001  0.20000000000000000E+001
kernel_type = pol
rcut = 2.0
desc_sparse = "gap_files/CH.xml.sparseX.GAP_2026_3_23_120_0_19_4_474"
alphas_sparse = "gap_files/alphas_angle_3b_1.dat"
gap_end

gap_beg angle_3b
species_center = C
species1 =  H
species2 = C
delta = 0.01
sigma = 0.20000000000000000E+001  0.20000000000000000E+001  0.20000000000000000E+001
kernel_type = pol
rcut = 2.0
desc_sparse = "gap_files/CH.xml.sparseX.GAP_2026_3_23_120_0_19_4_475"
alphas_sparse = "gap_files/alphas_angle_3b_2.dat"
gap_end

gap_beg angle_3b
species_center = C
species1 = C
species2 = C
delta = 0.01
sigma = 0.20000000000000000E+001  0.20000000000000000E+001  0.20000000000000000E+001
kernel_type = pol
rcut = 2.0
desc_sparse = "gap_files/CH.xml.sparseX.GAP_2026_3_23_120_0_19_4_476"
alphas_sparse = "gap_files/alphas_angle_3b_3.dat"
gap_end

gap_beg soap_turbo
n_species = 2
species =  H C
central_species = 1
rcut = 4.0 4.0
buffer = 0.5 0.5
atom_sigma_r = 0.2 0.2
atom_sigma_t = 0.2 0.2
atom_sigma_r_scaling = 0.1 0.1
atom_sigma_t_scaling = 0.1 0.1
amplitude_scaling = 2.0 2.0
n_max = 4 4
l_max = 4
nf = 4 4
central_weight = 1.0 1.0
scaling mode = polynomial
basis = "poly3gauss"
radial_enhancement = 1
zeta = 4
delta = 0.1
desc_sparse = "gap_files/CH.xml.sparseX.GAP_2026_3_23_120_0_19_4_477"
alphas_sparse = "gap_files/alphas_soap_turbo_1.dat"
compress_soap = .true.
compress_mode = "trivial"
gap_end

gap_beg soap_turbo
n_species = 2
species =  H C
central_species = 2
rcut = 4.0 4.0
buffer = 0.5 0.5
atom_sigma_r = 0.2 0.2
atom_sigma_t = 0.2 0.2
atom_sigma_r_scaling = 0.1 0.1
atom_sigma_t_scaling = 0.1 0.1
amplitude_scaling = 2.0 2.0
n_max = 4 4
l_max = 4
nf = 4 4
central_weight = 1.0 1.0
scaling mode = polynomial
basis = "poly3gauss"
radial_enhancement = 1
zeta = 4
delta = 0.1
desc_sparse = "gap_files/CH.xml.sparseX.GAP_2026_3_23_120_0_19_4_478"
alphas_sparse = "gap_files/alphas_soap_turbo_2.dat"
compress_soap = .true.
compress_mode = "trivial"
gap_end


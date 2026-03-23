#!/bin/bash

energy="energy"
virial="DUMMY"
forces="forces"



gap_fit atoms_filename=train_tagged.xyz core_param_file=pairpot_mod.xml core_ip_args={IP Glue} \
        gap={ \
              distance_2b Z1=1 Z2=1 cutoff=4.0 n_sparse=20 covariance_type=ard_se \
                  delta=0.5 theta_uniform=0.5 sparse_method=uniform add_species=F : \
              distance_2b Z1=1 Z2=6 cutoff=4.0 n_sparse=20 covariance_type=ard_se \
                  delta=0.5 theta_uniform=0.5 sparse_method=uniform add_species=F : \
              distance_2b Z1=6 Z2=6 cutoff=4.0 n_sparse=20 covariance_type=ard_se \
                  delta=0.5 theta_uniform=0.5 sparse_method=uniform add_species=F : \
              angle_3b Z_center=6 Z1=1 Z2=1 cutoff=2.0 n_sparse=100 covariance_type=pp \
                  delta=0.01 theta_uniform=2.0 sparse_method=uniform add_species=F : \
              angle_3b Z_center=6 Z1=1 Z2=6 cutoff=2.0 n_sparse=100 covariance_type=pp \
                  delta=0.01 theta_uniform=2.0 sparse_method=uniform add_species=F : \
              angle_3b Z_center=6 Z1=6 Z2=6 cutoff=2.0 n_sparse=100 covariance_type=pp \
                  delta=0.01 theta_uniform=2.0 sparse_method=uniform add_species=F : \
              soap_turbo l_max=4 alpha_max={{4 4}} atom_sigma_r={{0.2 0.2}} atom_sigma_t={{0.2 0.2}} \
                  atom_sigma_r_scaling={{0.1 0.1}} atom_sigma_t_scaling={{0.1 0.1}} \
                  zeta=4 rcut_hard=4.0 rcut_soft=3.5 basis=poly3gauss \
                  scaling_mode=polynomial add_species=F \
                  amplitude_scaling={{2.0 2.0}} n_species=2 species_Z={{1 6}} central_index=1 \
                  radial_enhancement=1 compress_mode=trivial \
                  central_weight={{1.0 1.0}} \
                  n_sparse=500 \
		  delta=0.1 f0=0.0 covariance_type=dot_product sparse_method=cur_points : \
              soap_turbo l_max=4 alpha_max={{4 4}} atom_sigma_r={{0.2 0.2}} atom_sigma_t={{0.2 0.2}} \
                  atom_sigma_r_scaling={{0.1 0.1}} atom_sigma_t_scaling={{0.1 0.1}} \
                  zeta=4 rcut_hard=4.0 rcut_soft=3.5 basis=poly3gauss \
                  scaling_mode=polynomial add_species=F \
                  amplitude_scaling={{2.0 2.0}} n_species=2 species_Z={{1 6}} central_index=2 \
                  radial_enhancement=1 compress_mode=trivial \
                  central_weight={{1.0 1.0}} \
                  n_sparse=500 \
		  delta=0.1 f0=0.0 covariance_type=dot_product sparse_method=cur_points : \
            } \
        default_sigma={0.001 0.1 0.1 0.1} \
        energy_parameter_name=${energy} force_parameter_name=${forces} \
        virial_parameter_name=${virial} \
        sparse_jitter=1.0e-8 e0={H:0:C:0} do_copy_at_file=F \
        sparse_separate_file=T openmp_chunk_size=10000 gp_file=CH.xml

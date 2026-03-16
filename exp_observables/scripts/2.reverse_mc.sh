workdir="2.reverse_mc"

rm -rf $workdir

mkdir -p $workdir

cp input_files/input_xps_optimization_gcmc ${workdir}/input

cp data/xps_spectra_interp.dat ${workdir}/

cp structures/melted_atoms.xyz ${workdir}/atoms.xyz

cd $workdir

ln -sf ../gap_files ./

mpirun -np 4 turbogap mc

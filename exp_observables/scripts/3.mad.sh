workdir="3.mad"

rm -rf $workdir

mkdir -p $workdir

cp input_files/input_xps_optimization_mad ${workdir}/input

cp xps_spectra_interp.dat ${workdir}/

cp structures/melted_atoms.xyz ${workdir}/atoms.xyz

cd $workdir

ln -sf ../gap_files ./

mpirun -np 4 turbogap md

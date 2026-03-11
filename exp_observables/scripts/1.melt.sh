workdir="1.melt"

rm -rf $workdir

mkdir -p $workdir

cp input_files/input_melt_graphite_CO ${workdir}/input

cp structures/atoms.xyz ${workdir}/

cd $workdir

ln -sf ../gap_files ./

mpirun -np 4 turbogap md

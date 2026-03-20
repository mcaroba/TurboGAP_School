workdir="5.gcmc-comp-1"

rm -rf $workdir
mkdir -p $workdir

cp input_files/input_gcmc-1 ${workdir}/input
cp structures/Cu55_Au3Pd_relax.xyz ${workdir}/atoms4.xyz

cd $workdir

ln -sf ../gap_files ./

mpirun -np 4 turbogap mc
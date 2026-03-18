workdir="4.gcmc-3"

rm -rf $workdir
mkdir -p $workdir

cp input_files/input_gcmc-3 ${workdir}/input
cp structures/atoms4.xyz ${workdir}/NP_AuPd3.xyz

cd $workdir

ln -sf ../gap_files ./

mpirun -np 4 turbogap mc
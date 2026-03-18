workdir="4.gcmc-2"

rm -rf $workdir
mkdir -p $workdir

cp input_files/input_gcmc-2 ${workdir}/input
cp structures/atoms4.xyz ${workdir}/NP_AuPd.xyz

cd $workdir

ln -sf ../gap_files ./

mpirun -np 4 turbogap mc
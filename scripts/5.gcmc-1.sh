workdir="5.gcmc-1"

rm -rf $workdir
mkdir -p $workdir

cp input_files/input_gcmc-1 ${workdir}/input
cp structures/atoms4.xyz ${workdir}/

cd $workdir

ln -sf ../gap_files ./

mpirun -np 3 turbogap mc
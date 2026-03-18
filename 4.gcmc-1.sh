workdir="4.gcmc-1"

rm -rf $workdir
mkdir -p $workdir

cp input_files/input_gcmc-1 ${workdir}/input
cp structures/PW.xyz ${workdir}/

cd $workdir

ln -sf ../gap_files ./

mpirun -np 4 turbogap mc
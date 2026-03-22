workdir="7.gcmc-exploration"

rm -rf $workdir
mkdir -p $workdir

cp input_files/your_input ${workdir}/input
cp structures/atoms4.xyz ${workdir}/

cd $workdir

ln -sf ../gap_files ./

mpirun -np 3 turbogap mc
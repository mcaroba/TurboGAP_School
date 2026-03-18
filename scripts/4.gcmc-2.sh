workdir="4.gcmc-2"

rm -rf $workdir
mkdir -p $workdir

cp input_files/input_gcmc-2 ${workdir}/input
cp structures/PW79_AuPd.xyz ${workdir}/

cd $workdir

ln -sf ../gap_files ./

mpirun -np 4 turbogap mc
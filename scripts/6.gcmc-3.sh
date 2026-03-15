workdir="6.gcmc-3"

rm -rf $workdir
mkdir -p $workdir

cp input_files/input_gcmc-3 ${workdir}/input
cp structures/PW79_dis_AuPd.xyz ${workdir}/

cd $workdir

ln -sf ../gap_files ./

mpirun -np 10 turbogap mc
workdir="7.my-run-1"

rm -rf $workdir
mkdir -p $workdir

cp input_files/your_input ${workdir}/input
cp structures/Cu55_AuPd_relax.xyz ${workdir}/atoms4.xyz

cd $workdir

ln -sf ../gap_files ./

mpirun -np 3 turbogap mc
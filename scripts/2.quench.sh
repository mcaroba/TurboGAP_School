workdir="2.quench"

rm -rf $workdir
mkdir -p $workdir

cp input_files/input_quench ${workdir}/input
cp structures/atoms1.xyz ${workdir}/

cd $workdir

ln -sf ../gap_files ./

mpirun -np 4 turbogap md
n=$(head -1 trajectory_out.xyz | awk '{print $1+2}')
tail -$n trajectory_out.xyz > atoms2.xyz
cp atoms2.xyz ../structures
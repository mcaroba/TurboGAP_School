workdir="3.relax"

rm -rf $workdir
mkdir -p $workdir

cp input_files/input_relax ${workdir}/input
cp structures/atoms2.xyz ${workdir}/

cd $workdir

ln -sf ../gap_files ./

mpirun -np 10 turbogap md
n=$(head -1 trajectory_out.xyz | awk '{print $1+2}')
tail -$n trajectory_out.xyz > atoms3.xyz
cp atoms3.xyz ../structures
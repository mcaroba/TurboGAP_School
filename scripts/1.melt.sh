workdir="1.melt"

rm -rf $workdir
mkdir -p $workdir

cp input_files/input_melt ${workdir}/input
cp structures/atoms0.xyz ${workdir}/

cd $workdir

ln -sf ../gap_files ./

mpirun -np 10 turbogap md
n=$(head -1 trajectory_out.xyz | awk '{print $1+2}')
tail -$n trajectory_out.xyz > atoms1.xyz
cp atoms1.xyz ../structures

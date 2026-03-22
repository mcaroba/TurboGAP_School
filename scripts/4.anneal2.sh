workdir="4.anneal2"

rm -rf $workdir
mkdir -p $workdir

cp input_files/input_anneal2 ${workdir}/input
cp structures/atoms3.xyz ${workdir}/

cd $workdir

ln -sf ../gap_files ./

mpirun -np 3 turbogap md
n=$(head -1 trajectory_out.xyz | awk '{print $1+2}')
tail -$n trajectory_out.xyz > atoms4.xyz
cp atoms4.xyz ../structures
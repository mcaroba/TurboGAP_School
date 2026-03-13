workdir="0.predict_large_graphite"

rm -rf $workdir

mkdir -p $workdir

cp input_files/input_predict_large_graphite ${workdir}/input

cp structures/graphite_large.xyz ${workdir}/atoms.xyz

cd $workdir

ln -sf ../gap_files ./

mpirun -np 4 turbogap predict

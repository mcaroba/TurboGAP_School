import numpy as np 
import sys 
import os 


def read_datablock( f  ):
    
    line = f.readline()

    n = len( line.split() ) 
    m = 0
    data = np.array([ float( s ) for s in line.split() ])
    m += 1 
    line = f.readline()
    while ( len( line.split() ) > 0 ):
        new_data = np.array([ float( s ) for s in line.split() ])
        data = np.vstack( (data, new_data) )
        m += 1 
        line = f.readline()

    return n, m, data

if ( len( sys.argv ) >= 2): 
    filename = sys.argv[1]

    if not os.path.exists( filename ): 
        print( "Error!! Cannot find the filename {filename}")
        exit(1)

else: 
    print( "Error!! You have not provided a file to plot! ")
    exit(1)


data = []

with open( filename, 'r' ) as f:
    # First line is always a comment, so we ignore
    f.readline()

    # usually the format is in x, y, (weight - optional)
    all_data = []
    n_data = 0
    while ( not f.read() is None  or f.read() != ""): 
        n, m, data = read_datablock(f) 
        all_data.append(data)
        n_data +=1 
        print(n, m, n_data)
print(all_data) 

    # line = f.readline()

    # n = len( line.split() ) 
    # m = 0
    # data = np.array([ float( s ) for s in line.split() ])
    # m += 1 
    # line = f.readline()
    # while ( len( line.split() ) > 0 ):
    #     new_data = np.array([ float( s ) for s in line.split() ])
    #     data = np.vstack( (data, new_data) )
    #     m += 1 
    #     line = f.readline()



    



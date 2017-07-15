# second Lab 

import numpy as np
import sys


a = np.arange(15).reshape(3,5) # my array

fn = 'demo_numpy.txt' # file name

with open(fn,'w') as f:   # opening the file name as write
    sys.stdout = f
    print("array:", a)
    print("array shape:", a.shape)
    print("array size:", a.size)
    print("array item size:", a.itemsize)
    print("array number of dimensions", a.ndim)
    print("array data type:", a.dtype)
            

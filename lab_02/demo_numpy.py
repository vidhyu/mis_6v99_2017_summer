# second Lab 

import numpy as np
import sys


a = np.arange(15).reshape(3,5) # my array

fn = 'demo_numpy.txt' # file name

with open(fn,'w') as f:   # opening the file name as write
    sys.stdout = f
    print(a)
    print(a.shape)
    print(a.size)
    print(a.itemsize)
    print(a.ndim)
    print(a.dtype)
            

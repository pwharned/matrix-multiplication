import numpy as np
a = np.ones(65536).reshape(256,256)
b = np.asarray(range(0,65536)).reshape(256,256)
a.dot(b.T)

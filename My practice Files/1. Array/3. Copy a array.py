import numpy as np
a=np.array([10,20,30,40,50])
b=np.zeros(len(a),dtype=int)
for i in range (len(a)):
    b[i]=a[i]
print(a)
print(b)
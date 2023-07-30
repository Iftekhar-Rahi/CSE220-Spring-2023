import numpy as np
arr=np.array([5,15,20,10])
def max(arr,x):
    if x==0:
        return arr[0]
    else:
        y=max(arr,x-1)
        if arr[x]>y:
            return arr[x]
        return y
print(max(arr,len(arr)-1))
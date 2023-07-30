import numpy as np
arr=np.array([5,15,20,10])
def max(arr,x):
    if x==0:
        return arr[0]
    else:
        y=max(arr,x-1)
        if y>arr[x]:
            return y
        return arr[x]
print(max(arr,len(arr)-1))
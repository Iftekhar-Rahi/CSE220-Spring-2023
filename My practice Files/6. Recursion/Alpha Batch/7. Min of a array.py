import numpy as np
arr=np.array([5,15,20,10])
def min(arr,x):
    if x==0:
        return arr[0]
    else:
        y=min(arr,x-1)
        if y<arr[x]:
            return y
        return arr[x]
print(min(arr,len(arr)-1))
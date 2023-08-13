import numpy as np
arr=np.array([10,20,30,40,50])
def printing_array(arr,n):
    if n==len(arr):
        return
    else:
        print(arr[n])
        printing_array(arr,n+1)
        return
printing_array(arr,0)
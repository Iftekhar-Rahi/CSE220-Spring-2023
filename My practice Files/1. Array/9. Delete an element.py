import numpy as np
arr=np.array([0,10,20,30,40,50])
def delete(arr,index=0):
    if 0<=index<len(arr):
        for i in range(index+1, len(arr)):
            arr[i-1] = arr[i]
        arr[len(arr)-1]=0
        print(arr)
    else:
        print("Invalid Index")
delete(arr,5)
import numpy as np
arr=np.array([10,20,30,40,50])
def left_shift(arr):
    temp=arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[len(arr)-1]=0
    print(arr)
left_shift(arr)
import numpy as np
arr=np.array([10,20,30,40,50,0])
def insert(arr,index,new_value):
    for i in range(len(arr)-1,index,-1):
        arr[i]=arr[i-1]
    arr[index]=new_value
    print(arr)
insert(arr,0,1)
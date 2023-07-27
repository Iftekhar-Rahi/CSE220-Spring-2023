arr=[10,20,30,40,50]
def right_rotate(arr):
    temp=arr[len(arr)-1]
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=temp
    print(arr)
right_rotate(arr)
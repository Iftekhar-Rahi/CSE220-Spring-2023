arr=[10,20,30,40,50]
def left_shift(arr):
    temp=arr[0]
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
    arr[len(arr)-1]=0
    print(arr)
left_shift(arr)
arr=[5,6,2,8]
def left_shift(arr):
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
    arr[len(arr)-1]=temp
    print(arr)
left_shift(arr)
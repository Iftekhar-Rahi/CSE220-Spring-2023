a=[10,20,30,40,50]
i=0
j=len(a)-1
#with while loop
# while i<=j:
#     temp=a[i]
#     a[i]=a[j]
#     a[j]=temp
#     i=i+1
#     j-=1
#with for loop
for i in range(len(a)//2):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    i = i + 1
    j -= 1
print(a)
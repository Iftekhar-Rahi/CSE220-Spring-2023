import numpy as np
# two_d_array=np.zeros((2,3),int)
# again=np.array([[1,2],[4,5]])
# print(again.shape)
# for r in range(2):
#     for c in range(2):
#         print(again[c][r],end=" ")
#     print()
again=np.array([[4,3,8],[2,5,1],[7,-1,9],[5,4,-2]])
# row,col=again.shape
# result=np.zeros(row,dtype=int)
# for r in range(row):
#     for c in range(col):
#         result[r]+=again[r][c]
# print(result)
# # min=result[0]
# for i in range(1,len(result)):
#     if result[i-1]<result[i]:
#         min=result[i-1]
#     else:
#         min=result[i]
# print(min)

row,col=again.shape
result=np.zeros(col,int)
for c in range(col):
    for r in range(row):
        result[c]+=again[r][c]
print(result)
def expo(x,n):
    if n==0:
        return 1
    else:
        # xnm1=expo(x,n-1)
        # xn=x*xnm1
        # return xn
        return x*expo(x,n-1)

print(expo(2,3))

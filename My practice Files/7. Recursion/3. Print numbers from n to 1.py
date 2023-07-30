def printdec(n):
    if n==1:
        print(n)
        return
    else:
        print(n, end=" ")
        printdec(n-1)
        return
printdec(10)

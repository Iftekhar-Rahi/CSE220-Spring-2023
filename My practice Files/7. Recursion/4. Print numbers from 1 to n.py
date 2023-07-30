def printInc(n):
    if n==1:
        print(n,end=" ")
        return
    else:
        printInc(n - 1)
        print(n,end=" ")
        return
printInc(10)
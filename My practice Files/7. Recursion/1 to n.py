def fun(n):
    if n == 1:
        print(1)
        return 1
    else:
        (fun(n-1))
        print(n)
fun(5)
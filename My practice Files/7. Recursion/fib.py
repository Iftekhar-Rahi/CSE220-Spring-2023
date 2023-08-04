def fib(n):
    if n==1 or n==2:
        return 1
    # elif n==2:
    #     return 1
    else:
        fib_1=fib(n-1)
        fib_2=fib(n-2)
        fib_n=fib_1+fib_2
        return fib_n
print(fib(5))
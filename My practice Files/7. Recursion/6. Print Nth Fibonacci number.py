def fib(n):
    if n==0 or n==1:
        return n
    else:
        fib_1=fib(n-1)
        fib_2=fib(n-2)
        fib_n=fib_1+fib_2
        return fib_n
print(fib(5))
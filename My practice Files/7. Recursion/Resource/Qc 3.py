def digit_counter(n,x):
    if n==0:
        return 0
    else:
        if n%10==x:
            return 1+digit_counter(n//10,x)
        else:
            return digit_counter(n//10,x)
print(digit_counter(987087697865976587657896,9))
def isPrime(num):
    divisor=helper(num,2)
    if divisor==0:
        return True
    else:
        return False

def helper(num,i=2):
    if num==i:
        return 0
    else:
        if num%i==0:
            return 1+helper(num,i+1)
        else:
            return helper(num, i + 1)

print(isPrime(18))
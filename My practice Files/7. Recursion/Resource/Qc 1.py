# n=int(input("Enter a number: ")) #126
# while n!=0: #1
#     last_digit=n%10 #1
#     print(last_digit)
#     n=n//10 #0

def sumDigits(n):
    if n==0:
        return 0
    else:
        return (n%10)+sumDigits(n//10)
print(sumDigits(12))
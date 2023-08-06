#1,2,3,4,5,6,7,8,9,
# 10
def bunnyEars2(n):
    if n==0:
        return 0
    else:
        if n%2==0:
            return 3+bunnyEars2(n-1)
        else:
            return 2 + bunnyEars2(n - 1)
print(bunnyEars2(3))
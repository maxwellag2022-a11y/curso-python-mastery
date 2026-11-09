# n! = 1 * 2 * 3 * 4 * ...... n
# 6! = 1 * 2 * 3 * 4 * 5 * 6

def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(6))
print(factorial(5))
print(factorial(4))
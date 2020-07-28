"""To print factorial of a number"""
def factorial(n):
    f = 1
    #consider each element till last element plus one
    for i in range(1,n+1):
        f = f*i
    return f

print(factorial(5))


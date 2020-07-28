"""decorators"""
def deco(func):
    def wrapper(*x):
        print("Before func is called")
        for i in x:
            if(i>0):
                print("valid numbers")
                res = func(*x)
                return res
        print("After func() is called")
    return wrapper

@deco
def add(*args):
    return sum(list(args))
print(add(-3,4,5))




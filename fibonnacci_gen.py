"""fibonnacci series using generators"""
def fib_gen(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b=b,a+b

#genobj=fib_gen(0)
#for i in genobj:
    #print(i)

"""fibonnacci series without generators"""
def fib(n):
    a,b = 0,1
    print(a)
    print(b)
    for i in range(2,n):
        c = a+b
        a = b
        b = c
        print(c)
print(fib(5))
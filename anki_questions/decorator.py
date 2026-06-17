
def decorator(func):
    def wrapper():
        print("calling the function ",func.__name__)
        func()
        print(func.__name__," has finished being called")
    
    return wrapper

@decorator
def print_hello():
    print("Hi")

print_hello()

# ADVANCED

def caching_function(f):
    cache = {}
    def wrapper(*args):
        if not args in cache:
            cache[args]=f(*args)
        return cache[args]
    return wrapper

@caching_function
def fib_func(a,b):

    while i <n:
        return fib(i)
    
    return fib_func()

def memoize(func):
    cache = {}                       # lives inside the closure
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args) # compute & store
        return cache[args]            # always return from cache
    return wrapper



@memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

fib(10)  # 11 calls  (vs 177 without memoisation)

fib(1)=1
fib(0)=0
fib(2)=1
fib(3)=2
fib(4)=3
fib(5)=5
fib(6)....

#Confusing, but cool that it can work backwards!

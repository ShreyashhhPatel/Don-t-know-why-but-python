from functools import wraps
import time

'DEECORATORS is A FUNCTION THAT TAKES ANOTHER FUNCTION AS AN ARGUMENT, ' \
'AND RETURNS A FUNCTION AS A RETURN VALUE'
def ticker(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()-t1
        print(f'P{func.__name__} ran in'\
              f'{t2}seconds')
    return wrapper

@ticker
def do_this():
    time.sleep(1.3)

@ticker
def do_that():
    time.sleep(.4)

do_this()
do_that()
print('done')
    
# Second decorator with parameters and wrapper

def add_sprinkers(func):
    def wrapper(*args,**kwargs):
        print("adding sprinkles")
        func(*args,**kwargs)        
    return wrapper

def add_fudge(func):
    # @wraps(func)  # This preserves the original function's metadata
    def wrapper(*args,**kwargs):
        print("adding fudge")
        func(*args,**kwargs)        
    return wrapper

@add_fudge
@add_sprinkers
def get_ice_cream(flavor):
    print(f"here is your {flavor} ice cream")

get_ice_cream('vanilla')



# #same without the wrapper
def add_syrups(func):
    print("adding syrups")
    func()    

@add_syrups
def get_ice_cream2():
    print("here is your ice cream")

print('-Its run without calling the function-')


#
#Lets use @wraps and why do we need it?
#
print("Lets use @wraps and why do we need it?")

from typing import Callable, Any

def get_time(func:callable) -> Callable:
    "Gets the time of the given function."
    @wraps(func) ###########this preserves the original function's metadata ########## (Comment out this line to see the difference in output)
    def wrapper(*args, **kwargs) -> Any:
        """Wrapper Docstring"""

        start_time : float = time.perf_counter()
        result: Any = func(*args, **kwargs)
        end_time: float = time.perf_counter()
        print(f'We ran the {func.__name__} in {start_time - end_time:.2f}seconds')
        return result
    return wrapper

@get_time
def expensive_function() -> None:
    """expensive_function() docstring"""
    time.sleep(2)
    print("done")


def main() -> None:
    print(expensive_function.__name__)
    print(expensive_function.__doc__)
    print(expensive_function.__annotations__)
    expensive_function()

if __name__ == "__main__":
    main()


import time
from functools import wraps

def retry(times=3, exceptions=(Exception,), delay=0):
    """Retry decorator.

    Args:
        times (int): Number of attempts.
        exceptions (tuple): Exceptions to catch.
        delay (int|float): Seconds to wait between retries.
    """
    def deco(fn):
        @wraps(fn)
        def w(*a, **k):
            last = None
            for i in range(1, times + 1):
                try:
                    return fn(*a, **k)
                except exceptions as e:
                    last = e
                    if i < times and delay > 0:
                        time.sleep(delay)
            raise last
        return w
    return deco

@retry(times=5, exceptions=(ValueError,), delay=1)
def test():
    print("Trying...")
    if time.time() % 2 < 1:
        raise ValueError("Failed!")
    return "Success!"

print(test())


# # Write @once so the function runs only on first call; later calls return the first result.
# Write @debug to log arguments and result of a function.
# Expected: prints like add(2,3) -> 5.

# def once(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print('doing something')
#         # wrapper.has_run = False
#         if not wrapper.has_run:
#             wrapper.value = func(*args, **kwargs)
#             wrapper.has_run = True
#         return wrapper.value
#     wrapper.has_run = False
#     wrapper.value = None
#     return wrapper  

def once(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.value = func(*args, **kwargs)
            wrapper.has_run = True
        return wrapper.value
    wrapper.has_run = False
    wrapper.value = None
    return wrapper

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}{args} -> {result}")
        return result
    return wrapper

@once
def init_value():
    print("Running init_value...")
    return 42

@debug
def add(a, b):
    return a + b


# Test @once
print(init_value())  # runs: prints "Running init_value...", returns 42
print(init_value())  # returns cached 42 without printing again

# Test @debug
add(2, 3)  # prints: add((2, 3), {}) -> 5
add(10, 20)  # prints: add((10, 20), {}) -> 30

# Example function that takes user input once
@once
def get_number():
    num = int(input("Enter a number: "))
    return num

# The first time you call it, it will ask for input
first_result = get_number()
print("First result:", first_result)

# The second time and onward, it will just return the same number without asking again
second_result = get_number()
print("Second result:", second_result)
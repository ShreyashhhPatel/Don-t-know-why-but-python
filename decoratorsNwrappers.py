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
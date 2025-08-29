x = 1
def outer():
    x = 2
    def inner():
        nonlocal x
        x += 1
        return x
    return inner

inc = outer()
print(inc(), inc(),inc())  

# Create make_counter(start=0) returning a function that increments and returns the count.
# Expected: successive calls: 1,2,3,... (from start).
def make_counter(start=0):
    count = start
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c1 = make_counter(40)
print(c1(), c1(), c1())

def count(start = 0):
    count = start

    def start_count():
        nonlocal  count
        count += 1
        return start_count
    return count
cz = count(3)
print(cz)

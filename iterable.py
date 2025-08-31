# def gen():
#     yield 1
#     yield from (2,3)
# for x in gen(): print(x)

def subgen():
    yield "A"
    yield "B"

def gen():
    yield 1
    # delegate to another generator
    yield from subgen()
    # delegate to a list
    yield from [2, 4, 6]
    # yield with some computation
    for i in range(3):
        yield f"computed-{i*i}"

for x in gen(): print(x)

def flatten(nested):
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)   # recursion + yield from
        else:
            yield item

nested = [1, [2, [3, 4], 5], 6]
print(list(flatten(nested)))

# Implement an infinite Fibonacci generator and print first 10 values.
# Expected: 0,1,1,2,3,5,8,13,21,34

def fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fibo()

for _ in range(10):
    print(next(f))
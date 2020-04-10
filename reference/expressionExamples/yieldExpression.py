def gen(value=None):
    yield 123
    yield 234

generator = gen()

for i in generator:
    print(i)

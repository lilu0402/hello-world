def Fib(num):
    a, b = 0, 1
    while num > 0:
        num -= 1
        yield b
        a, b = b, a + b


g = (i for i in Fib(10))

for i in range(10):
    print("%d:%d" % (i, next(g)))

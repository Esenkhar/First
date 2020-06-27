class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print('call {} to {} with args {}'.format(self.calls, self.func.__name__, args))
        self.func(*args)


@tracer
def spam(a, b, c):
    print(a, b, c)


@tracer
def spam2(a, b):
    print(a * b)


spam(1, 2, 3)
spam('a', 'b', 'c')
spam2(2, 3)
spam2('a', 3)

import os

print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
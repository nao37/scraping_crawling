import sys


def greet(name):
    print('Hello {}.'.format(name))


if len(sys.argv) > 1:
    name = sys.argv[1]
    greet(name)
else:
    name = 'world'
    greet(name)
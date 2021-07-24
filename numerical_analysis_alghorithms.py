from utils import function


def bisection_method():
    print('\nInput the values of a, b, e and the function f.')
    a = float(input('a: '))
    b = float(input('b: '))
    e = float(input('e: '))
    f = function()

    c = (a + b) / 2

    while abs(f.calc(c)) > e:
        if f.calc(a) * f.calc(c) > 0:
            a = c
        elif f.calc(a) * f.calc(c) < 0:
            b = c

        c = (a + b) / 2

    return c


def false_position_method():
    print('\nInput the values of a, b, e and the function f.')
    a = float(input('a: '))
    b = float(input('b: '))
    e = float(input('e: '))
    f = function()

    c = (a * f.calc(b) - b * f.calc(a)) / (f.calc(b) - f.calc(a))

    while abs(f.calc(c)) > e:
        if f.calc(a) * f.calc(c) > 0:
            a = c
        elif f.calc(a) * f.calc(c) < 0:
            b = c

        c = (a * f.calc(b) - b * f.calc(a)) / (f.calc(b) - f.calc(a))

    return c


def secant_method():
    print('\nInput the values of x0, x1, e and the function f.')
    xa = float(input('x0: '))  # x n-1
    xb = float(input('x1: '))  # x n
    xc = None                 # x n+1
    e = float(input('e: '))
    f = function()

    while abs(f.calc(xb)) > e:
        xc = xb - ((xb-xa) / (f.calc(xb) - f.calc(xa))) * f.calc(xb)
        xa = xb
        xb = xc

    return xb

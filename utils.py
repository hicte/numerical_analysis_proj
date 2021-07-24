import math 


def take_function():
    print('==========================================')
    expression = input('Enter the function as a valid python syntax:\nf(x) = ')
    print('==========================================')

    return expression


def calc_function(expression, x):
    try:
        y = eval(expression)
    except:
        print('Invalid expression!')
        return
    return y


class function:
    expression = None

    def __init__(self):
        self.expression = take_function()

    def calc(self, value):
        return calc_function(self.expression, value)

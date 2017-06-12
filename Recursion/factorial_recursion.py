# factorial recursion function

def factorial(value):
    '''
    factorial(1) = 1
    factorial(2) = 2
    factorial(3) = 6
    factorial(4) = 24
    factorial(5) = 120
    '''
    # a non-natural number is given
    if value <=0:
        raise IndexError
    # base case
    elif value <=2:
        return value
    # recursion
    # ex: factorial(4) would do: factorial(3)*4
    else:
        return factorial(value-1)*value

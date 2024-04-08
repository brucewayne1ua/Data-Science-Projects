from numba import jit


@jit
def Func():
    x = 5
    y = 6
    z = x+y
    return z

print (Func())
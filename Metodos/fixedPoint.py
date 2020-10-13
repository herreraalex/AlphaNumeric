import math

def f(x):
    return x**3 + 4 * x**2 - 10

def g(x):
    return math.sqrt(10/(x+4))

def fixedPoint(xa, iter, tol):
    fx = f(xa)
    cont = 0
    error = tol + 1
    xn = 0

    while((fx != 0) and error > tol and cont < iter):
        xn = g(xa)
        fx = f(xn)
        error = abs(xn - xa)
        xa = xn
        cont += 1
    
    if fx == 0:
        print("Xa: ", xa, " is a root")
    elif error < tol :
        print("Xa: ", xa, " approximate root with tolerance: ", tol)
    else:
        print("Fail in iteration: ", iter)

fixedPoint(1.5, 11, 0.000000005)
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**3 - np.cos(x)


def dF(x):
    return 3 * x**2 + np.sin(x)


def newton(x0, iter, tol):
    fx = f(x0)
    dFx = dF(x0)
    cont = 1
    error = tol + 1
    
    while( (fx != 0) and error > tol and (dFx != 0) and cont < iter):
        x1 = x0 - fx/dFx
        fx = f(x1)
        dFx = dF(x1)
        error = abs(x1-x0)
        x0 = x1
        cont += 1

    if fx == 0:
        print("X0: " ,x0, " is root")
    elif error < tol:
        print("X0: ", x0, " approximate root with tolerance: ", tol)
    elif dFx == 0:
        print("X0: ", x0, " is probably a multiple root")
    else:
        print("Fail in iteration: ", iter)


def draw():
    x = np.linspace(-2, 2, 100)
    plt.plot(x, x**3 - np.cos(x))
    plt.grid()
    plt.show()


newton(1, 10, 0.000000005)
draw()
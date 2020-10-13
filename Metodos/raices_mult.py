import sympy as sm
import math
import sys 
import json
import base64
import pandas as pd


def raices_mult(x0, nInteraciones, tol, funcion, funcion2, funcion3):
    results = {}
    x = sm.symbols('x')
    fx0 = sm.sympify(funcion).subs(x,x0)
    dfx0 = sm.sympify(funcion2).subs(x,x0)
    d2fx0 = sm.sympify(funcion3).subs(x,x0)

    cont = 0
    error = tol+1
    xn = 0
    det = (math.pow(dfx0,2)) - (fx0*d2fx0)
    results[cont] = [float(x0), float(fx0),float(0)]
    while (fx0 != 0 and error > tol and det != 0  and cont < nInteraciones):
        xn = x0 - ((fx0*dfx0)/det)
        fx0 = sm.sympify(funcion).subs(x,xn)
        dfx0 = sm.sympify(funcion2).subs(x,xn)
        d2fx0 = sm.sympify(funcion3).subs(x,xn)
        det = (math.pow(dfx0,2)) - (fx0*d2fx0)
        error = abs(xn-x0)
        x0 = xn
        cont = cont + 1
        results[cont] = [float(x0), float(fx0),float(error)]
    print_function(results)
    
    
    if(fx0 == 0):
        print(str(x0) + " es una raíz")

    elif(error < tol):
        print(str(x0) + " se encontró como una aproximación con una tolerancia de = " + str(tol))
    
    elif(det == 0):
         print("es una indeterminación")

    else:
         print("El método fracasó en " + str(nInteraciones) + " iteraciones")
    
def print_function(results):
    index = []
    x1 = []
    fprom = []
    error = []
    for i in results:
        index.append(i)
        x1.append(results[i][0])
        fprom.append(results[i][1])
        error.append(results[i][2])

    data = {
 
            'xi': x1,
            'F(xi)': fprom,
            'Error': error
            }
    df = pd.DataFrame(data, index=index)
    print(df)


raices_mult(1.0, 100, 0.00000001,"(exp(x))-x-1", '(exp(x))-1', 'exp(x)')

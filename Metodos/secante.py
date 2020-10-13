import sympy as sm
import math
import sys 
import json
import base64
import pandas as pd



def secante(x0, x1, nInteraciones, tol, funcion):
    results = {}

    x = sm.symbols('x')
    fx0 = sm.sympify(funcion).subs(x,x0)

    if(fx0 == 0):
        print(x0 + "es raíz" )
    else:
        fx1 = sm.sympify(funcion).subs(x,x1)
        cont = 1
        error = tol+1
        det = fx1 - fx0
        xi = 0
        results[cont-1] = [float(x0), float(fx0),float(0)]
        results[cont] = [float(x1), float(fx1),float(0)]
        while(fx1 != 0 and error > tol and det != 0 and cont < nInteraciones):

            xi = x1 - ((fx1*(x1-x0))/det)
            error = abs(xi-x1)
            x0 = x1
            fx0 = fx1
            x1 = xi
            fx1 = sm.sympify(funcion).subs(x,x1)
            det = fx1 - fx0
            cont = cont + 1
            results[cont] = [float(xi), float(fx1),float(error)]

        print_function(results)
        
           

        if(fx1 == 0):
           
            print(str(x0) + " se encontró como una raíz")
        

        elif(error < tol):
            print(str(x1) + " se encontró como aproximación con una tolerancia = " + str(tol))
        
        elif(det == 0):
            print(str(x1) + " es una posible raíz multiple")
        
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

secante(0.5, 1.0, 100, 0.0000001, 'ln((sin(x)^2)+1)-(1/2)')

        


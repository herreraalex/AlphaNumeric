import sympy as sm
import math
import sys
import json
import base64
import pandas as pd

def bisection(xi,xs,nIter,iter,funcion):

    if nIter > 0:
        results = {}
        x = sm.symbols('x')
        fxi = sm.sympify(funcion).subs(x,xi)
        fxs = sm.sympify(funcion).subs(x,xs)
        if (fxi == 0):
            print(fxi)
        elif(fxs == 0):
            print(fxa)
        elif(fxs*fxi < 0):
            xm = (xi + xs) / 2
            fxm = sm.sympify(funcion).subs(x,xm)
            count = 1
            error = iter + 1
            results[count] = [float(xi), float(xm), float(xs), float(fxm),float(error)]
            while((error > iter) and (count < nIter) ):
                if(fxi * fxm < 0):
                    xs = xm
                else:
                    xi = xm
                xaux = xm
                xm = (xi + xs) / 2
                fxm = sm.sympify(funcion).subs(x,xm)
                error = abs(xm-xaux)
                count += 1
                results[count] = [float(xi), float(xm), float(xs), float(fxm),float(error)]

            print_function(results)
            aux = json.dumps(results)
            print(results)
    else:
        print('el intervalo no sirve')
        sys.exit(1)

def print_function(results):
    index = []
    x1 = []
    x2 = []
    xprom = []
    fprom = []
    error = []
    for i in results:
        index.append(i)
        x1.append(results[i][0])
        xprom.append(results[i][1])
        x2.append(results[i][2])
        fprom.append(results[i][3])
        error.append(results[i][4])

    data = {'xi': x1,
            'xm': xprom,
            'xs': x2,
            'Fxm': fprom,
            'Error': error
            }
    df = pd.DataFrame(data, index=index)
    print(df)

bisection(0,1,100,0.0000001,'ln((sin(x)^2)+1)-(1/2)')


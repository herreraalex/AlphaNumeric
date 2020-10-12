import sympy as sm
import math
import sys
import json
import base64
import pandas as pd

def incremental_search(x_inicial, delta, limite_Iteraciones, funcion):
    if delta <= 0:
        print("El delta debe ser positivo")
        sys.exit(1)
    elif limite_Iteraciones > 0:
        resultados = {}
        x = sm.symbols('x')
        x_anterior = x_inicial
        x_actual = x_anterior+delta
        f_anterior = sm.sympify(funcion).subs(x,x_anterior)
        f_actual = sm.sympify(funcion).subs(x,x_actual)
        contador = 0
        while (contador < limite_Iteraciones):
            if f_actual*f_anterior<0:
                resultados[contador] = [x_anterior,x_actual]
            x_anterior = x_actual
            x_actual = x_actual + delta
            f_anterior = f_actual
            f_actual = sm.sympify(funcion).subs(x,x_actual)
            contador = contador + 1

        print_function(resultados)
        aux = json.dumps(resultados)

        print(aux)
    else:
        print("Las iteraciones deben ser un numero positivo")
        sys.exit(1)

def print_function(resultados):
    index = []
    x1 = []
    x2 = []
    for i in resultados:
        index.append(i)
        x1.append(resultados[i][0])
        x2.append(resultados[i][1])

    data = {'xi': x1,
            'xs': x2,
            }
    df = pd.DataFrame(data, index=index)
    print(df)

incremental_search(-3,0.5,100,'ln((sin(x)^2)+1)-(1/2)')
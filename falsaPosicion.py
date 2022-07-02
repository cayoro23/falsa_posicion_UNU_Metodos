import pandas as pd
from Grafico import Grafico
import matplotlib.pyplot as plt
import numpy as np


def _main(funcion, x_i, x_f, iteraciones, error_r) -> None:

    # Icicializar las variables
    solucion = None
    contador = 0
    error_calculado = 101
    ejesx = []
    ejesy = []
    solucioness = []
    erroress = []
    diccionario = {}

    # Evaluar si la raiz esta dentro del intervalo
    if funcion(x_i) * funcion(x_f) <= 0:

        # Calcular la solucion
        while contador <= iteraciones and error_calculado >= error_r:
            contador += 1

            # Formula de falsa posicion
            solucion = x_f - ((funcion(x_f) * (x_f - x_i)) /
                              (funcion(x_f) - funcion(x_i)))

            error_calculado = abs((solucion - x_i) / solucion) * 100

            # agregar eje x
            ejex = round(x_i, 5)

            # Reedefinir el nuevo intervalo
            if funcion(x_i) * funcion(solucion) >= 0:
                x_i = solucion
            else:
                x_f = solucion

            # Agregar a una variable
            ejey = round(x_f, 1)
            soluciones = round(solucion, 5)
            errores = error_calculado

            # Agregar a diccionario
            ejesx.append(ejex)
            ejesy.append(ejey)
            solucioness.append(soluciones)
            erroress.append(errores)

        diccionario['EJE X'] = ejesx
        diccionario['EJE Y'] = ejesy
        diccionario['SOLUCIONES'] = solucioness
        diccionario['ERRORES'] = erroress

        # Visualizar pandas
        datos = pd.DataFrame(diccionario)
        print(datos)

        grafico = Grafico(datos)
        grafico.agregarGrafico()

    else:
        print('-----------------------------------------')
        print("No existe solucion en ese intervalo")


if __name__ == '__main__':

    # Funcion a evaluar
    funcion = input('Ingrese la funcion a evaluar: ')
    parametroX = input('Ingrese el parametro X: ')
    parametroY = input('Ingrese el parametro Y: ')
    iteraciones = input('Ingrese el numero de iteraciones: ')
    error = input('Ingrese el error: ')

    # Iteraciones y Error si no se desea
    if iteraciones == '':
        iteraciones = 1000
    if error == '':
        error = 0.01

    # Enviar a la funcion
    _main(lambda x: eval(funcion), float(parametroX),
          float(parametroY), int(iteraciones), float(error))
    #  x: 4*x**4-9*x**2+1, 0, 1,5,0.01)

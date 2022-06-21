import pandas as pd


def _main(funcion, x_i, x_f, iteraciones, error_r) -> None:
    # Icicializar las variables
    solucion = None
    contador = 0
    error_calculado = 101
    # Evaluar si la raiz esta dentro del intervalo
    if funcion(x_i) * funcion(x_f) <= 0:
        # Calcular la solucion
        while contador <= iteraciones and error_calculado >= error_r:
            contador += 1
            solucion = x_f - ((funcion(x_f) * (x_f - x_i)) /
                              (funcion(x_f) - funcion(x_i)))
            error_calculado = abs((solucion - x_i) / solucion) * 100
            # Reedefinir el nuevo intervalo
            if funcion(x_i) * funcion(solucion) >= 0:
                x_i = solucion
            else:
                x_f = solucion


            array1 = []

            nombre = solucion
            edad = error_calculado
            lista = [nombre, edad]
            array1.append(lista)

        # # Imprimir el resultado

        #     print('-----------------------------------------')
        #     print('La solucion aproximada es: {:.5f}'.format(solucion))
        #     print('Encontrada en: {:.0f}'.format(contador)+' iteraciones')
        #     print('Con un error relativo de: {:.1f}'.format(error_calculado)+'%')

    else:
        print('-----------------------------------------')
        print("No existe solucion en ese intervalo")


mostrarPanda(array1)


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
    #  x**3 + 4*(x**2)-10, 1, 2)


def mostrarPanda(array1):
    data = pd.DataFrame(array1, columns=['EJE X', 'EJE Y'])

    print(data)

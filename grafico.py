import matplotlib.pyplot as plt


class Grafico:
    def __init__(self, datos):
        self.datos = datos

    def agregarGrafico(self):
        # Graficar
        fig, ax = plt.subplots(2, 2, sharey=True)
        ax[0, 0].plot(self.datos['EJE X'], marker='^',
                      color='tab:orange', label='EJE X')
        ax[0, 1].plot(self.datos['EJE Y'], marker='o',
                      color='tab:red', label='EJE Y')
        ax[1, 0].plot(self.datos['SOLUCIONES'], marker='*',
                      color='tab:blue', label='SOLUCIONES')
        ax[1, 1].plot(self.datos['ERRORES'], marker='+',
                      color='tab:green', label='ERRORES')
        # Agregar etiquetas
        ax[0, 0].legend(loc='upper right')
        ax[0, 1].legend(loc='upper right')
        ax[1, 0].legend(loc='upper right')
        ax[1, 1].legend(loc='upper right')
        # Mostrar grafico
        plt.show()

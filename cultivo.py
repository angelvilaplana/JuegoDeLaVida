import copy
from random import randint

from celula import Celula


class Cultivo:

    def __init__(self, tammano=30):
        self.tammano = tammano
        self._celulas = []
        self.celulas_vivas = 0
        self.celulas_muertas = 0

    @property
    def tammano(self):
        """
        El tamaño del cultivo
        """
        return self._tammano

    @tammano.setter
    def tammano(self, tammano=30):
        if tammano < 10:
            raise ValueError('El cultivo debe ser >= 10')
        else:
            self._tammano = tammano

    def generate(self):
        """
        Generamos el cultivo con
        valores random
        """
        self.celulas_vivas = 0
        self.celulas_muertas = 0

        for i in range(0, self._tammano):
            self._celulas.append([])
            for j in range(0, self._tammano):
                cel = Celula()
                cel.estado = randint(0, 1)
                if cel.estado:
                    self.celulas_vivas += 1
                else:
                    self.celulas_muertas += 1
                self._celulas[i].append(cel)

    def get_vecinos(self, x, y):
        """
        Obtener las celulas vecinas
        de la posición de la celula

        :param x: Posición de la celula en el eje x
        :param y:  Posición de la celula en el eje y
        :return: Número de vecinos vivos
        """
        vecinos = self._celulas[(x - 1) % self._tammano][(y - 1) % self._tammano].estado + \
                  self._celulas[x % self._tammano][(y - 1) % self._tammano].estado + \
                  self._celulas[(x + 1) % self._tammano][(y - 1) % self._tammano].estado + \
                  self._celulas[(x - 1) % self._tammano][y % self._tammano].estado + \
                  self._celulas[(x + 1) % self._tammano][y % self._tammano].estado + \
                  self._celulas[(x - 1) % self._tammano][(y + 1) % self._tammano].estado + \
                  self._celulas[x % self._tammano][(y + 1) % self._tammano].estado + \
                  self._celulas[(x + 1) % self._tammano][(y + 1) % self._tammano].estado

        return vecinos

    def update(self):
        """
        Actualiza el cultivo comprobando las celulas
        en cada celda
        """
        celulas_aux = copy.deepcopy(self._celulas)
        self.celulas_vivas = 0
        self.celulas_muertas = 0

        for i in range(self._tammano):
            for j in range(self._tammano):
                vecinos = self.get_vecinos(j, i)
                if self._celulas[j][i].esta_viva(vecinos):
                    celulas_aux[j][i].viva()
                    self.celulas_vivas += 1
                else:
                    celulas_aux[j][i].muerta()
                    self.celulas_muertas += 1

        self._celulas[:] = celulas_aux[:]

    def show(self):
        """
        Mostrar el cultivo
        """
        for i in range(self._tammano):
            for j in range(self._tammano):
                cel = self._celulas[i][j]
                print(cel, end=" ")
            print()

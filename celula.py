class Celula:

    def __init__(self, estado=0):
        self.estado = estado

    @property
    def estado(self):
        """
        El estado es la vida de la Celula
        estado = 0 -> muerta
        estado = 1 -> viva
        """
        return self._estado

    @estado.setter
    def estado(self, estado=0):
        if estado == 0 or estado == 1:
            self._estado = estado
        else:
            raise ValueError('El estado debe ser 0 o 1')

    def viva(self):
        """
        Para cambiar el estado
        de la celula a viva
        """
        self._estado = 1

    def muerta(self):
        """
        Para cambiar el estado
        de la celula a muerta
        """
        self._estado = 0

    def esta_viva(self, vecinos):
        """
        Comprobar si en la siguiente generación
        la celula esta viva
        """

        if 0 <= vecinos <= 8:
            """
            Comprobar el número de vecinos introducidos
            por parametro
            """

            if self._estado == 0 and vecinos == 3:
                """
                Si esta muerto y tiene 3 vecinos, la celula vive
                """
                return True
            elif vecinos == 2:
                """
                Si tiene 2 vecinos, cambia el estado de la celula
                """
                return not self._estado
            else:
                """
                Si no cumple con ninguna condición anterior,
                seguira en el mismo estado
                """
                return self._estado
        else:
            raise ValueError('El valor debe ser un número entre [0,8]')

    def __str__(self):
        return str(self._estado)

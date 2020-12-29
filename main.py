import csv
import time

from cultivo import Cultivo


FIELDNAMES_CSV = ['Turno', 'Celulas vivas', 'Celulas muertas']


def input_turnos():
    """
    Input donde debemos introducir el número de turnos
    que queramos que tenga el juego de la vida

    :return: Devuelve el número de turnos
    """
    while True:
        try:
            turnos = int(input("Introduce el número de turnos: "))
            if turnos <= 0:
                raise ValueError
            return turnos
        except ValueError:
            print("Introduce un número válido mayor a 0")


def input_csv():
    """
    Input donde indicamos si queremos guardar los
    resultados en un archivo CSV y el nombre del archivo

    :return: Devuelve el nombre del archivo si se introduce
             Si se dice que no devolvera "None"
    """
    opcion = input("¿Deseas guadar los resultados en un archivo csv? (s/n): ")
    if opcion.lower() == 's':
        nombre_archivo = input("Introduzca el nombre del archivo: ")
        nombre_archivo += ".csv"

        with open(nombre_archivo, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES_CSV)
            writer.writeheader()

        return nombre_archivo
    else:
        return None


def show_info(cultivo):
    """
    Imprinir la información del cultivo

    :param cultivo: El cultivo donde obtenemos
                    la información
    """
    print("Celulas vivas:", cultivo.celulas_vivas)
    print("Celulas muerta:", cultivo.celulas_muertas)


def save_data(nombre_archivo, turno, cultivo):
    with open(nombre_archivo, "a+", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES_CSV)
        writer.writerow({'Turno': turno,
                         'Celulas vivas': cultivo.celulas_vivas,
                         'Celulas muertas': cultivo.celulas_muertas})


if __name__ == '__main__':
    turnos = input_turnos()
    nombre_archivo = input_csv()

    cultivo = Cultivo()
    cultivo.generate()

    for i in range(1, turnos + 1):
        print("\nTURNO", i, end="\n\n")
        cultivo.show()

        print()
        show_info(cultivo)
        print()

        if nombre_archivo is not None:
            save_data(nombre_archivo, i, cultivo)

        if i + 1 != turnos + 1:
            time.sleep(1)
            cultivo.update()

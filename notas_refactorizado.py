# programa para calcular la media de tres notas y mostrar notas y resultados de aprobado/suspenso
# Autor: Ricarly Escalona
# fecha: 2026-03-02

def calcular_media(nota1, nota2, nota3):
    """
    Calcula la media aritmética de tres notas.

    Args:
        nota1 (float): Primera nota del alumno.
        nota2 (float): Segunda nota del alumno.
        nota3 (float): Tercera nota del alumno.

    Returns:
        float: La media de las tres notas.
    """
    return (nota1 + nota2 + nota3) / 3


def esta_aprobado(media):
    """Muestra si la media está aprobada o suspendida y devuelve un booleano.

    Args:
        media (float): Media ya calculada de las notas.

    Returns:
        bool: True si está aprobada (>=5), False si está suspendida.
    """
    if media >= 5:
        print("aprobado")
        return True
    else:
        print("suspendido")
        return False


def mostrar_informe_alumno(nombre, nota1, nota2, nota3):
    """Muestra la información completa de un alumno y su calificación.

    Args:
        nombre (str): Nombre del alumno.
        nota1 (float): Primera nota del alumno.
        nota2 (float): Segunda nota del alumno.
        nota3 (float): Tercera nota del alumno.

    Returns:
        float: La media de las tres notas.
    """
    print("Alumno: " + nombre)
    print("Nota 1: " + str(nota1))
    print("Nota 2: " + str(nota2))
    print("Nota 3: " + str(nota3))

    media = calcular_media(nota1, nota2, nota3) # Calculamos la media de las tres notas
    print("Media: " + str(media))

    # Clasificamos la nota según el valor de la media

    if media >= 9:
        print("Sobresaliente")
    elif media >= 7:
        print("Notable")
    elif media >= 5:
        print("Aprobado")
    else:
        print("Suspenso")

    # Reutilizamos la lógica de aprobado/suspenso
    esta_aprobado(media)

    print("----------------------")


def main():
    mostrar_informe_alumno("Ana García", 8, 7, 9)
    mostrar_informe_alumno("Luis Pérez", 4, 5, 3)
    mostrar_informe_alumno("Marta Gómez", 6, 7, 5)
    mostrar_informe_alumno("José Braganza", 4, 5, 7.5)
    mostrar_informe_alumno("Carlos Ruiz", 7, 3, 5)

main()
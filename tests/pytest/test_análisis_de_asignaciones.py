from asignacion_aulica.backend import análisis_de_asignaciones as análisis
from helper_functions import *

def test_ningún_aula_chica():
    clases = make_clases(
        dict(cantidad_de_alumnos = 10),
        dict(cantidad_de_alumnos = 25),
        dict(cantidad_de_alumnos = 80)
    )
    aulas = make_aulas(
        dict(capacidad = 30),
        dict(capacidad = 100),
        dict(capacidad = 10) # Esta queda justito para la clase 0
    )
    asignaciones = [2, 0, 1]

    aulas_chicas = análisis.clases_con_aula_chica(clases, aulas, asignaciones)
    assert len(aulas_chicas) == 0

def test_algún_aula_chica():
    clases = make_clases(
        dict(cantidad_de_alumnos = 10),
        dict(cantidad_de_alumnos = 25),
        dict(cantidad_de_alumnos = 80)
    )
    aulas = make_aulas(
        dict(capacidad = 30),
        dict(capacidad = 10) # Esta queda justito para la clase 0
    )
    asignaciones = [1, 0, 0]

    aulas_chicas = análisis.clases_con_aula_chica(clases, aulas, asignaciones)
    assert aulas_chicas == {2}

def test_todas_las_aulas_chicas():
    clases = make_clases(
        dict(cantidad_de_alumnos = 50),
        dict(cantidad_de_alumnos = 25),
        dict(cantidad_de_alumnos = 80)
    )
    aulas = make_aulas(
        dict(capacidad = 24),
        dict(capacidad = 10)
    )
    asignaciones = [0, 0, 1]

    aulas_chicas = análisis.clases_con_aula_chica(clases, aulas, asignaciones)
    assert aulas_chicas == {0, 1 ,2}

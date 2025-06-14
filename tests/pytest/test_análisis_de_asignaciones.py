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

    clases_excedidas = análisis.clases_con_aula_chica(clases, aulas, asignaciones)
    assert len(clases_excedidas) == 0

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

    clases_excedidas = análisis.clases_con_aula_chica(clases, aulas, asignaciones)
    assert clases_excedidas == {2: 80-30}

def test_todas_las_clases_excedidas():
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

    clases_excedidas = análisis.clases_con_aula_chica(clases, aulas, asignaciones)
    assert clases_excedidas == {0: 50-24, 1: 25-24, 2: 80-10}

def test_todas_fuera_del_edificio_preferido():
    clases = make_clases(
        dict(edificio_preferido = '1'),
        dict(edificio_preferido = '3'),
        dict(edificio_preferido = '2'),
        dict(edificio_preferido = '1'),
    )
    aulas = make_aulas(
        dict(edificio = '2'),
        dict(edificio = '1'),
        dict(edificio = '2'),
        dict(edificio = '3'),
        dict(edificio = '3'),
        dict(edificio = '1'),
        dict(edificio = '2'),
    )
    asignaciones = [0, 1, 4, 3]

    clases_tristes = análisis.clases_fuera_del_edificio_preferido(clases, aulas, asignaciones)
    assert clases_tristes == {0, 1, 2, 3}

def test_una_sola_en_el_edificio_preferido():
    clases = make_clases(
        dict(edificio_preferido = '1'),
        dict(edificio_preferido = '3'),
        dict(edificio_preferido = '2'),
        dict(edificio_preferido = '1'),
    )
    aulas = make_aulas(
        dict(edificio = '2'),
        dict(edificio = '1'),
        dict(edificio = '2'),
        dict(edificio = '3'),
        dict(edificio = '3'),
        dict(edificio = '1'),
        dict(edificio = '2'),
    )
    asignaciones = [0, 1, 2, 3]

    clases_tristes = análisis.clases_fuera_del_edificio_preferido(clases, aulas, asignaciones)
    assert clases_tristes == {0, 1, 3}

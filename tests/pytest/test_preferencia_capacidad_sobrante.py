from ortools.sat.python import cp_model
import numpy as np
import pytest

from asignacion_aulica.backend.restricciones import no_superponer_clases
from asignacion_aulica.backend import preferencias
from helper_functions import make_aulas, make_clases, make_asignaciones

def test_algunas_clases_les_sobra_capacidad():
    aulas = make_aulas(
        dict(capacidad=31),
        dict(capacidad=50),
        dict(capacidad=100)
    )
    clases = make_clases(
        dict(cantidad_de_alumnos=30),
        dict(cantidad_de_alumnos=40),
        dict(cantidad_de_alumnos=25),
    )
    modelo = cp_model.CpModel()

    # Forzar asignaciones arbitrarias (clase i con aula i)
    asignaciones = make_asignaciones(clases, aulas, modelo, asignaciones_forzadas={ 0: 0, 1: 1, 2: 2 })

    cantidad_sobrante, cota_superior = preferencias.obtener_capacidad_sobrante(clases, aulas, modelo, asignaciones)

    # Resolver
    solver = cp_model.CpSolver()
    status = solver.solve(modelo)
    if status != cp_model.OPTIMAL:
        pytest.fail(f'El solver terminó con status {solver.status_name(status)}. Alguien escribió mal la prueba.')
    
    assert solver.value(cantidad_sobrante) == (31 - 30 + 50 - 40 + 100 - 25)
    assert cota_superior == (100 - 30 + 100 - 40 + 100 - 25)

def test_ninguna_clase_le_sobra_capacidad():
    aulas = make_aulas(
        dict(capacidad=31),
        dict(capacidad=50),
        dict(capacidad=100)
    )
    clases = make_clases(
        dict(cantidad_de_alumnos=250),
        dict(cantidad_de_alumnos=400),
        dict(cantidad_de_alumnos=100),
    )
    modelo = cp_model.CpModel()

    # Forzar asignaciones arbitrarias (clase i con aula i)
    asignaciones = make_asignaciones(clases, aulas, modelo, asignaciones_forzadas={ 0: 0, 1: 1, 2: 2 })

    cantidad_sobrante, cota_superior = preferencias.obtener_capacidad_sobrante(clases, aulas, modelo, asignaciones)

    # Resolver
    solver = cp_model.CpSolver()
    status = solver.solve(modelo)
    if status != cp_model.OPTIMAL:
        pytest.fail(f'El solver terminó con status {solver.status_name(status)}. Alguien escribió mal la prueba.')
    
    assert solver.value(cantidad_sobrante) == 0
    # La cota superior sería 0, pero en cambio se devuelve 1 porque si no
    # fallaría al normalizar, siendo que debe dividir por la cota superior
    assert cota_superior == 1

def test_entran_justito():
    aulas = make_aulas(
        dict(capacidad=10),
        dict(capacidad=20),
        dict(capacidad=30)
    )
    clases = make_clases(
        dict(cantidad_de_alumnos=10),
        dict(cantidad_de_alumnos=20),
        dict(cantidad_de_alumnos=30),
    )
    modelo = cp_model.CpModel()

    asignaciones = make_asignaciones(clases, aulas, modelo)

    # Restricciones para que no estén en el mismo aula
    for predicado in no_superponer_clases(clases, aulas, {}, asignaciones):
        modelo.add(predicado)

    # Minimizar capacidad sobrante
    cantidad_sobrante, cota_superior = preferencias.obtener_capacidad_sobrante(clases, aulas, modelo, asignaciones)
    modelo.minimize((1 / cota_superior) * cantidad_sobrante)

    # Resolver
    solver = cp_model.CpSolver()
    status = solver.solve(modelo)
    if status != cp_model.OPTIMAL:
        pytest.fail(f'El solver terminó con status {solver.status_name(status)}. Alguien escribió mal la prueba.')
    asignaciones_finales = np.vectorize(solver.value)(asignaciones)
    
    assert solver.value(cantidad_sobrante) == 0
    assert cota_superior == (30 - 10 + 30 - 20 + 30 - 30)
    assert sum(asignaciones_finales[0,:]) == 1 and asignaciones_finales[0, 0] == 1
    assert sum(asignaciones_finales[1,:]) == 1 and asignaciones_finales[1, 1] == 1
    assert sum(asignaciones_finales[2,:]) == 1 and asignaciones_finales[2, 2] == 1

def test_minimiza_capacidad_sobrante():
    '''
    Esta prueba es para verificar que minimiza la capacidad sobrante en total, y
    no el número de aulas con capacidad sobrante.

    La idea es que si minimizara el número de aulas pondría la materia más
    chica en el aula más grande y quedaría mucha gente afuera. En cambio si
    minimiza la gente que queda afuera, queda menos gente afuera.
    '''
    aulas = make_aulas(
        dict(capacidad=11),
        dict(capacidad=21),
        dict(capacidad=31)
    )

    clases = make_clases(
        dict(cantidad_de_alumnos=10),
        dict(cantidad_de_alumnos=20),
        dict(cantidad_de_alumnos=30),
    )
    modelo = cp_model.CpModel()

    asignaciones = make_asignaciones(clases, aulas, modelo)

    # Restricciones para que no estén en el mismo aula
    for predicado in no_superponer_clases(clases, aulas, {}, asignaciones):
        modelo.add(predicado)

    # Minimizar capacidad sobrante
    cantidad_sobrante, cota_superior = preferencias.obtener_capacidad_sobrante(clases, aulas, modelo, asignaciones)
    modelo.minimize((1 / cota_superior) * cantidad_sobrante)

    # Resolver
    solver = cp_model.CpSolver()
    status = solver.solve(modelo)
    if status != cp_model.OPTIMAL:
        pytest.fail(f'El solver terminó con status {solver.status_name(status)}. Alguien escribió mal la prueba.')
    asignaciones_finales = np.vectorize(solver.value)(asignaciones)

    assert solver.value(cantidad_sobrante) == 3
    assert cota_superior == (31 - 10 + 31 - 20 + 31 - 30)
    assert sum(asignaciones_finales[0,:]) == 1 and asignaciones_finales[0, 0] == 1
    assert sum(asignaciones_finales[1,:]) == 1 and asignaciones_finales[1, 1] == 1
    assert sum(asignaciones_finales[2,:]) == 1 and asignaciones_finales[2, 2] == 1


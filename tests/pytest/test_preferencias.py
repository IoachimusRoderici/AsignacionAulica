from ortools.sat.python import cp_model
import pytest

from asignacion_aulica.backend import preferencias, lógica_de_asignación
from helper_functions import *

def test_todas_las_aulas_en_el_edificio_preferido():
    aulas = make_aulas(
        dict(edificio='preferido'),
        dict(edificio='preferido'),
        dict(edificio='preferido')
    )
    edificios = {'preferido': aulas.index}

    clases, modelo = make_clases(
        len(aulas),
        dict(edificio_preferido='preferido'),
        dict(edificio_preferido='preferido')
    )

    clases_fuera_del_edificio_preferido = preferencias.obtener_cantidad_de_clases_fuera_del_edificio_preferido(modelo, clases, edificios)

    # Forzar asignaciones arbitrarias
    modelo.add(clases.loc[0, 'aula_asignada'] == 1)
    modelo.add(clases.loc[1, 'aula_asignada'] == 2)

    # Resolver
    solver = cp_model.CpSolver()
    status = solver.solve(modelo)
    if status != cp_model.OPTIMAL:
        pytest.fail(f'El solver terminó con status {solver.status_name(status)}. Alguien escribió mal la prueba.')
    
    assert solver.value(clases_fuera_del_edificio_preferido) == 0

def test_algunas_aulas_en_el_edificio_preferido():
    aulas = make_aulas(
        dict(edificio='preferido'),
        dict(edificio='no preferido'),
        dict(edificio='preferido'),
        dict(edificio='preferido 2')
    )
    edificios = lógica_de_asignación.construir_edificios(aulas)

    clases, modelo = make_clases(
        len(aulas),
        dict(edificio_preferido='preferido'),
        dict(edificio_preferido='preferido'),
        dict(edificio_preferido='preferido 2'),
        dict(edificio_preferido='preferido'),
        dict(edificio_preferido='preferido 2'),
        dict(edificio_preferido='preferido')
    )

    clases_fuera_del_edificio_preferido = preferencias.obtener_cantidad_de_clases_fuera_del_edificio_preferido(modelo, clases, edificios)

    # Forzar asignaciones arbitrarias (generadas aleatoriamente)
    modelo.add(clases.loc[0, 'aula_asignada'] == 3)
    modelo.add(clases.loc[1, 'aula_asignada'] == 2)
    modelo.add(clases.loc[2, 'aula_asignada'] == 1)
    modelo.add(clases.loc[3, 'aula_asignada'] == 1)
    modelo.add(clases.loc[4, 'aula_asignada'] == 2)
    modelo.add(clases.loc[5, 'aula_asignada'] == 0)

    # Resolver
    solver = cp_model.CpSolver()
    status = solver.solve(modelo)
    if status != cp_model.OPTIMAL:
        pytest.fail(f'El solver terminó con status {solver.status_name(status)}. Alguien escribió mal la prueba.')
    
    assert solver.value(clases_fuera_del_edificio_preferido) == 4
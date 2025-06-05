from ortools.sat.python import cp_model
import pytest

from asignacion_aulica.backend import preferencias
from helper_functions import *

def test_algunas_clases_exceden_capacidad():
    aulas = make_aulas(
        dict(capacidad=30),
        dict(capacidad=40),
        dict(capacidad=25)
    )

    clases, modelo = make_clases(
        len(aulas),
        dict(cantidad_de_alumnos=31),
        dict(cantidad_de_alumnos=50),
        dict(cantidad_de_alumnos=100),
    )

    cantidad_excedida = preferencias.obtener_cantidad_de_alumnos_fuera_del_aula(modelo, clases, aulas)

    # Forzar asignaciones arbitrarias
    modelo.add(clases.loc[0, 'aula_asignada'] == 0)
    modelo.add(clases.loc[1, 'aula_asignada'] == 1)
    modelo.add(clases.loc[2, 'aula_asignada'] == 2)

    # Resolver
    solver = cp_model.CpSolver()
    status = solver.solve(modelo)
    if status != cp_model.OPTIMAL:
        pytest.fail(f'El solver terminó con status {solver.status_name(status)}. Alguien escribió mal la prueba.')
    
    assert solver.value(cantidad_excedida) == (31 - 30 + 50 - 40 + 100 - 25)

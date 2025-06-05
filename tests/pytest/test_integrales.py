from asignacion_aulica import backend
from helper_functions import *

def test_restricciones_y_preferencias():
    '''
    Prueba que las restricciones tienen prioridad sobre las preferencias,
    y las penalizaciones son minimizadas.
    '''

    aulas = make_aulas(
        dict(capacidad=60),
        dict(capacidad=40, equipamiento={"proyector"}),
    )

    clases, _ = make_clases(
        len(aulas),
        dict(día="lunes", cantidad_de_alumnos=70, equipamiento_necesario={"proyector"}),
        dict(día="lunes", cantidad_de_alumnos=50),
        dict(día="miércoles", cantidad_de_alumnos=56),
        dict(día="miércoles", cantidad_de_alumnos=55),
    )

    asignaciones = backend.asignar(aulas, clases)
    asignaciones_esperadas = [1, 0, 0, 1]

    for asignación, asignación_esperada in zip(asignaciones, asignaciones_esperadas):
        assert asignación == asignación_esperada


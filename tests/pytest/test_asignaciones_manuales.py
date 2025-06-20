from helper_functions import *

from asignacion_aulica.backend.restricciones import no_asignar_aulas_ocupadas

from asignacion_aulica.backend.lógica_de_asignación import separar_asignaciones_manuales

def test_separar_asignaciones_manuales():
    clases = make_clases(
        dict(aula_asignada=1, día=Día.LUNES, horario_inicio=10, horario_fin=15),
        dict(),
        dict(aula_asignada=33, día=Día.JUEVES, horario_inicio=255, horario_fin=322),
        dict(),
        dict()
    )
    
    clases_sin_asignar, indices_sin_asignar, aulas_ocupadas = separar_asignaciones_manuales(clases)

    assert len(clases_sin_asignar) == 3
    assert all(clases_sin_asignar['aula_asignada'].isnull())
    assert list(clases_sin_asignar.index) == [0, 1, 2] # Verificar que los índices se re-generaron

    assert indices_sin_asignar == [1, 3, 4]

    assert aulas_ocupadas == {(33, Día.JUEVES, 255, 322), (1, Día.LUNES, 10, 15)}

def test_dos_clases_al_mismo_tiempo_con_una_asignación_manual():
    aulas = make_aulas(
        {},
        {}
    )
    clases = make_clases(
        dict(horario_inicio=10, horario_fin=13, día=Día.LUNES),
        dict(horario_inicio=10, horario_fin=13, día=Día.LUNES, aula_asignada=0)
    )
    modelo = cp_model.CpModel()
    
    # Probar no_asignar_aulas_ocupadas
    clases_sin_asignar, indices_sin_asignar, asignaciones_manuales = separar_asignaciones_manuales(clases)
    prohibidas = list(no_asignar_aulas_ocupadas(clases_sin_asignar, aulas, {(1, Día.LUNES, 10, 13)}))

    assert prohibidas == [(0, 1)]

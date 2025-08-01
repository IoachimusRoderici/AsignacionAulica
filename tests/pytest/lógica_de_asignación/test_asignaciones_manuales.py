import pytest

from asignacion_aulica.lógica_de_asignación.asignar import separar_asignaciones_manuales, asignar
from asignacion_aulica.lógica_de_asignación.restricciones import no_asignar_aulas_ocupadas
from asignacion_aulica.lógica_de_asignación import ImposibleAssignmentException
from asignacion_aulica.lógica_de_asignación.dia import Día

@pytest.mark.clases(
    dict(aula_asignada=1, día=Día.LUNES, horario_inicio=10, horario_fin=15),
    dict(),
    dict(aula_asignada=33, día=Día.JUEVES, horario_inicio=255, horario_fin=322),
    dict(),
    dict()
)
def test_separar_asignaciones_manuales(clases):
    clases_sin_asignar, índices_sin_asignar, aulas_ocupadas = separar_asignaciones_manuales(clases)

    assert len(clases_sin_asignar) == 3
    assert all(clases_sin_asignar['aula_asignada'].isnull())
    assert list(clases_sin_asignar.index) == [0, 1, 2] # Verificar que los índices se re-generaron

    assert índices_sin_asignar == [1, 3, 4]

    assert aulas_ocupadas == {(33, Día.JUEVES, 255, 322), (1, Día.LUNES, 10, 15)}

@pytest.mark.aulas({}, {}, {})
@pytest.mark.clases(
    dict(día=Día.MARTES, horario_inicio=19, horario_fin=23),
    dict(día=Día.MARTES, horario_inicio=20, horario_fin=22, aula_asignada=1)
)
def test_asignación_manual_al_aula_doble(aulas, clases):
    '''
    Verificar que si se asigna manualmente al aula doble, las aulas individuales
    también se bloquean en ese horario.
    '''
    aulas_dobles = {1: (0, 2)}

    # Probar separar_asignaciones_manuales
    clases_sin_asignar, índices_sin_asignar, aulas_ocupadas = separar_asignaciones_manuales(clases)
    assert len(clases_sin_asignar) == 1
    assert índices_sin_asignar == [0]
    assert aulas_ocupadas == {(1, Día.MARTES, 20, 22)}

    # Probar no_asignar_aulas_ocupadas
    prohibidas = set(no_asignar_aulas_ocupadas(clases_sin_asignar, aulas, aulas_dobles, aulas_ocupadas))
    assert (0, 1) in prohibidas
    assert (0, 0) in prohibidas
    assert (0, 2) in prohibidas

    # Probar asignar
    with pytest.raises(ImposibleAssignmentException):
        asignar(clases, aulas, aulas_dobles)

@pytest.mark.aulas({}, {})
@pytest.mark.clases(
    dict(día=Día.LUNES, horario_inicio=10, horario_fin=13),
    dict(día=Día.LUNES, horario_inicio=10, horario_fin=13, aula_asignada=0)
)
def test_dos_clases_al_mismo_tiempo_con_una_asignación_manual(aulas, clases):
    aulas_dobles = {}
    
    # Probar separar_asignaciones_manuales
    clases_sin_asignar, índices_sin_asignar, aulas_ocupadas = separar_asignaciones_manuales(clases)
    assert len(clases_sin_asignar) == 1
    assert índices_sin_asignar == [0]
    assert aulas_ocupadas == {(0, Día.LUNES, 10, 13)}
    
    # Probar no_asignar_aulas_ocupadas
    prohibidas = set(no_asignar_aulas_ocupadas(clases_sin_asignar, aulas, aulas_dobles, aulas_ocupadas))
    assert prohibidas == {(0, 0)}

    # Probar asignar
    asignar(clases, aulas)
    assert all( clases['aula_asignada'] == [1, 0] )

@pytest.mark.aulas({}, {}, {})
@pytest.mark.clases(
    dict(día=Día.LUNES,   horario_inicio=10, horario_fin=13, aula_asignada=1),
    dict(día=Día.LUNES,   horario_inicio=10, horario_fin=13), # Mismo horario
    dict(día=Día.DOMINGO, horario_inicio=10, horario_fin=13), # Mismo horario pero otro día
    dict(día=Día.LUNES,   horario_inicio=11, horario_fin=12), # Superposición completa
    dict(día=Día.LUNES,   horario_inicio= 9, horario_fin=11), # Parcialmente antes
    dict(día=Día.LUNES,   horario_inicio=12, horario_fin=15), # Parcialmente después
    dict(día=Día.LUNES,   horario_inicio=13, horario_fin=16), # Mismo día y se tocan justo
    dict(día=Día.LUNES,   horario_inicio=17, horario_fin=20), # Mismo día pero otro horario
)
def test_una_asignación_y_varias_superposiciones(aulas, clases):
    aulas_dobles = {}

    # Probar separar_asignaciones_manuales
    clases_sin_asignar, índices_sin_asignar, aulas_ocupadas = separar_asignaciones_manuales(clases)
    assert len(clases_sin_asignar) == 7
    assert índices_sin_asignar == list(range(1,8))
    assert aulas_ocupadas == {(1, Día.LUNES, 10, 13)}
    
    # Probar no_asignar_aulas_ocupadas
    prohibidas = set(no_asignar_aulas_ocupadas(clases_sin_asignar, aulas, aulas_dobles, aulas_ocupadas))
    assert prohibidas == {(0, 1), (2, 1), (3, 1), (4, 1)}

    # Probar asignar
    asignar(clases, aulas)
    assert clases.at[0, 'aula_asignada'] == 1
    assert all ( clases.loc[[1, 2, 3, 4], 'aula_asignada'] != 1 )

@pytest.mark.aulas(*[{}]*10) # Re críptico pero esto significa 10 aulas con valores default
@pytest.mark.clases(
    dict(día=Día.MARTES, horario_inicio=10, horario_fin=13),
    dict(día=Día.MARTES, horario_inicio=10, horario_fin=13, aula_asignada=1), # Mismo horario
    dict(día=Día.JUEVES, horario_inicio=10, horario_fin=13, aula_asignada=2), # Mismo horario pero otro día
    dict(día=Día.MARTES, horario_inicio=11, horario_fin=12, aula_asignada=3), # Superposición completa
    dict(día=Día.MARTES, horario_inicio= 9, horario_fin=11, aula_asignada=4), # Parcialmente antes
    dict(día=Día.MARTES, horario_inicio=12, horario_fin=15, aula_asignada=5), # Parcialmente después
    dict(día=Día.MARTES, horario_inicio=13, horario_fin=16, aula_asignada=6), # Mismo día y se tocan justo
    dict(día=Día.MARTES, horario_inicio=17, horario_fin=20, aula_asignada=7), # Mismo día pero otro horario
)
def test_varias_asignaciones_y_una_no_asignada(aulas, clases):
    aulas_dobles = {}

    # Probar separar_asignaciones_manuales
    clases_sin_asignar, índices_sin_asignar, aulas_ocupadas = separar_asignaciones_manuales(clases)
    assert len(clases_sin_asignar) == 1
    assert índices_sin_asignar == [0]
    assert aulas_ocupadas == {
        (1, Día.MARTES, 10, 13),
        (2, Día.JUEVES, 10, 13),
        (3, Día.MARTES, 11, 12),
        (4, Día.MARTES,  9, 11),
        (5, Día.MARTES, 12, 15),
        (6, Día.MARTES, 13, 16),
        (7, Día.MARTES, 17, 20),
    }

    # Probar no_asignar_aulas_ocupadas
    prohibidas = set(no_asignar_aulas_ocupadas(clases_sin_asignar, aulas, aulas_dobles, aulas_ocupadas))
    assert prohibidas == {(0, 1), (0, 3), (0, 4), (0, 5)}

    # Probar asignar
    asignar(clases, aulas)
    assert clases.at[0, 'aula_asignada'] not in {1, 3, 4, 5}
    assert all( clases.at[i, 'aula_asignada'] == i for i in range(1,8) )

@pytest.mark.aulas(
    dict(),
    dict(horarios={Día.MARTES: (7, 20)}),
    dict(),
    dict(capacidad=20, equipamiento={'pizarrón'}),
)
@pytest.mark.clases(
    dict(día=Día.MIÉRCOLES), # No se superpone con ninguna de las asignaciones manuales
    dict(día=Día.MARTES, horario_inicio=10, horario_fin=13, aula_asignada=1), # Mismo aula al mismo tiempo
    dict(día=Día.MARTES, horario_inicio=11, horario_fin=12, aula_asignada=1),
    dict(día=Día.SÁBADO, horario_inicio=15, horario_fin=19, aula_asignada=0), # Aula doble y aula individual al mismo tiempo
    dict(día=Día.SÁBADO, horario_inicio=18, horario_fin=20, aula_asignada=3),
    dict(día=Día.MARTES, horario_inicio=19, horario_fin=23, aula_asignada=1), # Asignadas a un aula cerrada
    dict(día=Día.VIERNES, aula_asignada=1),
    dict(día=Día.JUEVES, cantidad_de_alumnos=30, aula_asignada=3), # Capacidad insuficiente
    dict(día=Día.JUEVES, equipamiento_necesario={'pizarrón', 'proyector'}, aula_asignada=3), # Equipamiento insuficiente
)
def test_asignaciones_manuales_que_inclumplen_restricciones(aulas, clases):
    '''
    Verificar que se respetan las asignaciones manuales aunque no cumplan con
    algunas restricciones
    '''
    aulas_dobles = {0: (2, 3)}
    
    asignar(clases, aulas, aulas_dobles)
    assert clases.at[0, 'aula_asignada'] in aulas.index # Verificar que se asignó algún aula
    assert clases.at[1, 'aula_asignada'] == 1
    assert clases.at[2, 'aula_asignada'] == 1
    assert clases.at[3, 'aula_asignada'] == 0
    assert clases.at[4, 'aula_asignada'] == 3
    assert clases.at[5, 'aula_asignada'] == 1
    assert clases.at[6, 'aula_asignada'] == 1
    assert clases.at[7, 'aula_asignada'] == 3
    assert clases.at[8, 'aula_asignada'] == 3

@pytest.mark.aulas(*[{}]*5) # Re críptico pero esto significa 5 aulas con valores default
@pytest.mark.clases(
    dict(aula_asignada=1),
    dict(aula_asignada=3),
    dict(aula_asignada=0),
    dict(aula_asignada=2),
    dict(aula_asignada=4),
    dict(aula_asignada=1),
    dict(aula_asignada=1),
)
def test_todas_las_aulas_asignadas_manuales(aulas, clases):
    '''
    Verificar que cuando todas las asignaciones son manuales, se maneja
    correctamente (no saltan excepciones ni se cambian las asignaciones).
    '''

    asignar(clases, aulas)

    assert clases.at[0, 'aula_asignada'] == 1
    assert clases.at[1, 'aula_asignada'] == 3
    assert clases.at[2, 'aula_asignada'] == 0
    assert clases.at[3, 'aula_asignada'] == 2
    assert clases.at[4, 'aula_asignada'] == 4
    assert clases.at[5, 'aula_asignada'] == 1
    assert clases.at[6, 'aula_asignada'] == 1


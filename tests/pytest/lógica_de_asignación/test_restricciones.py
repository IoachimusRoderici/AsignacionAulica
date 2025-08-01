import pytest
from verificación_de_predicados import predicado_es_nand_entre_dos_variables_bool

from asignacion_aulica.lógica_de_asignación import restricciones
from asignacion_aulica.lógica_de_asignación.dia import Día

@pytest.mark.aulas({})
@pytest.mark.clases(
        dict(horario_inicio=1, horario_fin=3),
        dict(horario_inicio=2, horario_fin=4),
        dict(horario_inicio=5, horario_fin=6)
    )
def test_superposición(aulas, clases, asignaciones):
    predicados = list(restricciones.no_superponer_clases(clases, aulas, {}, asignaciones))

    # Debería generar solamente un predicado entre las primeras dos clases
    assert len(predicados) == 1
    predicado = predicados[0]
    assert predicado_es_nand_entre_dos_variables_bool(predicado)
    assert asignaciones[0,0] in predicado.vars
    assert asignaciones[1,0] in predicado.vars

@pytest.mark.clases( dict(horario_inicio=10, horario_fin=13, día=Día.LUNES) )
@pytest.mark.aulas(
    dict(horarios={Día.LUNES: (10, 13)}), # Igual que la clase
    dict(horarios={Día.LUNES: (10, 11)}), # Cierra temprano
    dict(horarios={Día.LUNES: (11, 13)}), # Abre tarde
    dict(horarios={Día.LUNES: (9, 14)}),  # Sobra
    dict(horarios={Día.LUNES: (11, 12)}), # Abre tarde y cierra temprano
    dict(horarios={Día.MARTES: (9, 14)}), # No abre los lunes
)
def test_aulas_cerradas(clases, aulas):
    prohibidas = list(restricciones.no_asignar_en_aula_cerrada(clases, aulas))

    # Debería generar restricciones con las aulas 1, 2, 4 y 5
    assert len(prohibidas) == 4
    assert (0, 1) in prohibidas
    assert (0, 2) in prohibidas
    assert (0, 4) in prohibidas
    assert (0, 5) in prohibidas

@pytest.mark.clases( dict(cantidad_de_alumnos = 50) )
@pytest.mark.aulas(
    dict(capacidad = 100),
    dict(capacidad = 50),
    dict(capacidad = 10)
)
def test_capacidad_suficiente(clases, aulas):
    prohibidas = list(restricciones.asignar_aulas_con_capacidad_suficiente(clases, aulas))

    # Debería generar una sola restricción con el aula 2
    assert len(prohibidas) == 1
    assert (0, 2) in prohibidas

@pytest.mark.clases( dict(equipamiento_necesario = set(('proyector',))) )
@pytest.mark.aulas(
    dict(equipamiento = set(('proyector',))),
    dict(equipamiento = set(('proyector', 'otra cosa'))),
    dict(equipamiento = set())
)
def test_equipamiento(clases, aulas):
    prohibidas = list(restricciones.asignar_aulas_con_el_equipamiento_requerido(clases, aulas))

    # Debería generar una sola restricción con el aula 2
    assert len(prohibidas) == 1
    assert (0, 2) in prohibidas

@pytest.mark.aulas(
    dict(nombre = '102A'),
    dict(nombre = '102B'),
    dict(nombre = '102')
)
@pytest.mark.clases(
    dict(nombre = 'Clase 1'),
    dict(nombre = 'Clase 2')
)
def test_aulas_dobles(aulas, clases, asignaciones): 
    # 102 es un aula doble conformada por 102A y 102B
    aulas_dobles = { 2: (0, 1) }

    predicados = list(restricciones.no_asignar_aula_doble_y_sus_hijas_al_mismo_tiempo(clases, aulas, aulas_dobles, asignaciones))

    assert len(predicados) == 4
    for predicado in predicados:
        assert predicado_es_nand_entre_dos_variables_bool(predicado)
    assert any(asignaciones[0, 2] in predicado.vars and asignaciones[1, 0] in predicado.vars  for predicado in predicados)
    assert any(asignaciones[0, 2] in predicado.vars and asignaciones[1, 1] in predicado.vars  for predicado in predicados)
    assert any(asignaciones[1, 2] in predicado.vars and asignaciones[0, 0] in predicado.vars  for predicado in predicados)
    assert any(asignaciones[1, 2] in predicado.vars and asignaciones[0, 1] in predicado.vars  for predicado in predicados)

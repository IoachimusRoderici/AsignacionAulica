import pytest, random, logging

from asignacion_aulica.lógica_de_asignación.dia import Día
from asignacion_aulica import lógica_de_asignación

def aulas_params_generator(aulas_count: int, capacidad_max: int, edificios_count: int):
    '''
    Genera parámetros para la creación de aulas.
    Las capacidades de las aulas se generan pseudo-aleatoriamente, pero con una
    semilla fija para que sea consistente.

    :param aulas_count: Cantidad de aulas a generar.
    :param capacidad_max: Capacidad máxima exclusiva para un aula.
    :param edificios_count: Cantidad total de edificios.
    :return: Tupla de diccionarios para el fixture `aulas`.
    '''
    # Dar semilla para que siempre sean los mismo números
    random.seed(0)
    aulas_params = []

    for i in range(aulas_count):
        aulas_params.append({
            'capacidad': random.randrange(1, capacidad_max),
            # Garantiza que haya al menos un aula por edificio (si aulas_count >= edificios_count)
            'edificio': i % edificios_count,
        })

    return aulas_params

def clases_params_generator(amount_per_hour: int, cantidad_de_alumnos_max: int, edificios_count: int):
    '''
    Genera parámetros para la creación de clases.
    Las cantidades de alumnos y los edificios preferidos de las clases se
    generan pseudo-aleatoriamente, pero con una semilla fija para que sea
    consistente.

    :param amount_per_hour: Cantidad de clases a generar por cada hora de la semana.
        Debe ser menor o igual a la cantidad de aulas generadas para que la
        asignación sea posible.
    :param cantidad_de_alumnos_max: Cantidad máxima exclusiva de alumnos.
    :param edificios_count: Cantidad total de edificios.
    :return: Tupla de diccionarios para el fixture `aulas`.
    '''
    # Dar semilla para que siempre sean los mismo números
    random.seed(1)
    clases_params = []

    for día in Día:
        for hora in range(0, 24):
            horario_inicio = hora
            horario_fin = hora + 1
            for i in range(amount_per_hour):
                clases_params.append({
                    'día': día,
                    'horario_inicio': horario_inicio,
                    'horario_fin': horario_fin,
                    'cantidad_de_alumnos': random.randrange(1, cantidad_de_alumnos_max),
                    'edificio_preferido': random.randrange(edificios_count),
                })

    logging.info(f'Cantidad de clases: {len(clases_params)}.')

    return clases_params

@pytest.mark.stress_test
@pytest.mark.aulas(
    *aulas_params_generator(
        aulas_count=10,
        capacidad_max=100,
        edificios_count=10
    )
)
@pytest.mark.clases(
    *clases_params_generator(
        amount_per_hour=10,
        cantidad_de_alumnos_max=100,
        edificios_count=10
    )
)
def test_small_stress(aulas, clases):
    lógica_de_asignación.asignar(clases, aulas)

@pytest.mark.stress_test
@pytest.mark.aulas(
    *aulas_params_generator(
        aulas_count=20,
        capacidad_max=100,
        edificios_count=10
    )
)
@pytest.mark.clases(
    *clases_params_generator(
        amount_per_hour=20,
        cantidad_de_alumnos_max=100,
        edificios_count=10
    )
)
def test_medium_stress(aulas, clases):
    lógica_de_asignación.asignar(clases, aulas)

@pytest.mark.stress_test
@pytest.mark.aulas(
    *aulas_params_generator(
        aulas_count=30,
        capacidad_max=100,
        edificios_count=10
    )
)
@pytest.mark.clases(
    *clases_params_generator(
        amount_per_hour=30,
        cantidad_de_alumnos_max=100,
        edificios_count=10
    )
)
def test_large_stress(aulas, clases):
    lógica_de_asignación.asignar(clases, aulas)

@pytest.mark.stress_test
@pytest.mark.aulas(
    *aulas_params_generator(
        aulas_count=30,
        capacidad_max=100,
        edificios_count=10
    )
)
@pytest.mark.clases(
    *clases_params_generator(
        amount_per_hour=31,
        cantidad_de_alumnos_max=100,
        edificios_count=10
    )
)
def test_large_stress_asignación_imposible(aulas, clases):
    with pytest.raises(lógica_de_asignación.ImposibleAssignmentException):
        lógica_de_asignación.asignar(clases, aulas)


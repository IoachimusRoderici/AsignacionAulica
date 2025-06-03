'''
Este módulo resuelve el problema lógico de asignación de aulas
usando el solucionador de restricciones `ortools`.

Ver manual de ortools: https://developers.google.com/optimization/cp

Se define un modelo con los siguientes componentes:
- Variables: Cada variable es el número de aula que tiene asignada una clase.
  El número de aula 0 significa que no tiene asignada un aula.

- Restricciones: Cada restricción es una condición booleana que se tiene que
  cumplir para que la asignación de aulas sea correcta.

- Penalizaciones: Son un puntaje que se asigna a las situaciones que preferimos
  evitar si es posible, aunque no generen una asignación de aulas incorrecta.

Luego se usa el solver para encontrar una combinación de variables que cumpla
con todas las restricciones y que tenga la menor penalización posible.
'''
from ortools.sat.python import cp_model
from pandas import DataFrame
from typing import Iterable

from .impossible_assignment_exception import ImposibleAssignmentException
from .restricciones import todas_las_restricciones
from .preferencias import obtener_penalizaciones

def asignar(aulas: DataFrame, clases: DataFrame) -> tuple[ list[int], dict[str, int] ]:
    '''
    Resolver el problema de asignación.

    :param aulas: Tabla con los datos de todas las aulas disponibles.
        Columnas:
        - edificio: str
        - nombre: str
        - capacidad: int
        - equipamiento: set[str]
        - horario_apertura: int #TODO: Decidir cómo representar los horarios en números enteros
        - horario_cierre: int
    :param clases: Tabla con los datos de todas las clases.
        Una clase por fila.
        Columnas:
        - nombre: str (materia y comisión)
        - día: str (de la semana)
        - horario_inicio: int
        - horario_fin: int
        - cantidad_de_alumnos: int
        - equipamiento_necesario: set[str]
        - edificio_preferido: str
    :return: Una lista con el número de aula asignada a cada clase, y un
        diccionario con los valores de las penalizaciones.
    :raise ImposibleAssignmentException: Si no es posible hacer la asignación.
    '''
    # Modelo que contiene las variables, restricciones, y penalizaciones
    modelo = cp_model.CpModel()
    
    # Agregar al modelo una variable por cada clase, que representa el
    # número de aula que tiene asignada esa clase.
    max_aula = len(aulas) - 1
    clases = clases.copy()
    clases['aula_asignada'] = [modelo.new_int_var(0, max_aula, f'aula_clase_{i}') for i in clases.index]
    
    # Agregar al modelo las restricciones
    for predicado in todas_las_restricciones(clases, aulas):
        modelo.add(predicado)

    # Agregar al modelo las penalizaciones
    penalizaciones = obtener_penalizaciones(modelo, clases, aulas)
    modelo.minimize(penalizaciones['total'])

    # Resolver
    solver = cp_model.CpSolver()
    status = solver.solve(modelo)
    status_name = solver.status_name(status)
    if status_name not in 'OPTIMAL':
        raise ImposibleAssignmentException(f'El solucionador de restricciones terminó con status {status_name}.')
    
    #TODO: ¿qué hacer si da FEASIBLE?¿en qué condiciones ocurre?¿aceptamos la solución suboptima o tiramos excepción?

    cantidad_de_clases_fuera_del_edificio_preferido = solver.value(cantidad_de_clases_fuera_del_edificio_preferido)
    print(f"{cantidad_de_clases_fuera_del_edificio_preferido=}")

    # Armar lista con las asignaciones
    aulas_asignadas = list(map(solver.value, clases['aula_asignada']))
    
    # Armar diccionario con los valores de las penalizaciones
    penalizaciones_evaluadas = {key: solver.value(value) for key, value in penalizaciones.items()}
    penalizaciones_evaluadas.pop('total')
    
    return aulas_asignadas, penalizaciones_evaluadas
  

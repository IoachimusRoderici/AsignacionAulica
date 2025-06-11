'''
Este módulo resuelve el problema lógico de asignación de aulas
usando el solucionador de restricciones CP-SAT de `ortools`.

Ver manual de ortools: https://developers.google.com/optimization/cp

Se define un modelo (CpModel) con los siguientes componentes:
- Matriz de variables de asignación: Es una matriz donde cada fila representa
  una clase, cada columna representa un aula, y cada celda contiene un booleano
  que indica si esa clase está asignada a ese aula.

  Los booleanos están codificados como 0 (False) o 1 (True) porque así lo pide
  la interfaz de ortools. Algunas celdas contienen constantes (asignaciones
  fijas) y otras contienen variables del modelo (asignaciones a ser resueltas
  por ortools).

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
from .preferencias import obtener_penalización
import restricciones

def asignar(aulas: DataFrame, clases: DataFrame) -> list[int]:
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
    :return: Una lista con el número de aula asignada a cada clase.
    :raise ImposibleAssignmentException: Si no es posible hacer la asignación.
    '''
    # Crear modelo, variables, restricciones, y penalizaciones
    modelo = cp_model.CpModel()
    asignaciones = crear_matriz_de_asignaciones(aulas, clases)

    for predicado in restricciones.restricciones_con_variables(clases, aulas, asignaciones):
        modelo.add(predicado)
    
    penalización = obtener_penalización(modelo, clases, aulas, asignaciones)
    modelo.minimize(penalización)

    # Resolver
    solver = cp_model.CpSolver()
    status = solver.solve(modelo)
    #TODO: ¿qué hacer si da FEASIBLE?¿en qué condiciones ocurre?¿aceptamos la solución suboptima o tiramos excepción?
    if status != cp_model.OPTIMAL:
        raise ImposibleAssignmentException(f'El solucionador de restricciones terminó con status {solver.status_name(status)}.')
    
    # Armar lista con las asignaciones
    asignaciones_finales = np.vectorize(solver.value)(asignaciones)
    aulas_asignadas = list((asignaciones_finales!=0).argmax(axis=1))
        
    return aulas_asignadas
  

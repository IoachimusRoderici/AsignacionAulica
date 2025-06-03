'''
En este módulo se definen las preferencias del sistema de asignación.

Las preferencias son valores numéricos que dependen de las variables del modelo,
y que se quieren minimizar o maximizar. En particular este módulo define
penalizaciones, que son preferencias que se quieren minimizar.

Cada penalización se define en una función que agrega al modelo las variables
necesarias y devuelve una expresión que representa el valor a minimizar.

Estas funciones toman los siguientes argumentos:
- modelo: el CpModel al que agregar variables
- clases: DataFrame, tabla con los datos de las clases
- aulas: DataFrame, tabla con los datos de las aulas

Esto se omite de los docstrings para no tener que repetirlo en todos lados.

Las penalizaciones individuales se suman para formar una penalización total.
Cada penalización tiene un peso distinto en esa suma, para permitir darle más
importancia a unas que a otras.

La función `obtener_penalizaciones` es la que hay que llamar desde fuera de este
módulo. Devuelve un diccionario con todas las penalizaciones, incluyendo una
llamada "total" que es la que hay que minimizar.
'''
from ortools.sat.python import cp_model
from pandas import DataFrame
from typing import Iterable

def construir_edificios(aulas: DataFrame) -> dict[str, set[int]]:
    '''
    Devuelve el diccionario de nombres de edificio a set de aulas que tiene cada edificio.
    '''
    edificios = {}
    for aula in aulas.itertuples():
        if not aula.edificio in edificios:
            edificios[aula.edificio] = set((aula.Index,))
        else:
            edificios[aula.edificio].add(aula.Index)

    return edificios

def obtener_cantidad_de_clases_fuera_del_edificio_preferido(modelo: cp_model.CpModel, clases: DataFrame, aulas: DataFrame):
    '''
    Agrega al modelo variables booleanas que representan si una clase está fuera de su edificio preferido.
    Devuelve la suma de esas variables, que representa la cantidad de clases fuera de su edificio preferido.
    '''
    edificios = construir_edificios(aulas)
    cantidad_de_clases_fuera_del_edificio_preferido = 0

    for clase in clases.itertuples():
        aulas_del_edificio_preferido_en_un_formato_re_raro = [(aula,) for aula in edificios[clase.edificio_preferido]]

        # Definir flag de edificio preferido en el modelo
        fuera_del_edificio_preferido = modelo.new_bool_var(f"{clase.nombre}_fuera_del_edificio_preferido")
        modelo.add_allowed_assignments([clase.aula_asignada], aulas_del_edificio_preferido_en_un_formato_re_raro).only_enforce_if(~fuera_del_edificio_preferido)
        modelo.add_forbidden_assignments([clase.aula_asignada], aulas_del_edificio_preferido_en_un_formato_re_raro).only_enforce_if(fuera_del_edificio_preferido)

        cantidad_de_clases_fuera_del_edificio_preferido += fuera_del_edificio_preferido

    return cantidad_de_clases_fuera_del_edificio_preferido

# Iterable de tuplas (peso, nombre, función)
todas_las_penalizaciones = (
    (10, 'cantidad de clases fuera del edificio preferido', obtener_cantidad_de_clases_fuera_del_edificio_preferido),
)

def obtener_penalizaciones(modelo: cp_model.CpModel, clases: DataFrame, aulas: DataFrame):
    '''
    Calcula todas las penalizaciones.

    Agrega al modelo las variables necesarias y devuelve un diccionario con
    toas las expresiones de penalizaciones.

    :param modelo: El CpModel al que agregar variables.
    :param clases: Tabla con los datos de las clases.
    :param aulas: Tabla con los datos de las aulas.
    :return: Diccionario que mapea nombres de penalizaciones a expresiones que
        las representan. La penalización con el nombre "total" es la que el
        modelo tiene que minimizar, las demás pueden servir para informar al
        usuario sus valores luego de la asignación.
    '''
    penalizaciones = {}
    penalización_total = 0
    for peso, nombre, función in todas_las_penalizaciones:
        expresión = función(modelo, clases, aulas)
        penalizaciones[nombre] = expresión
        penalización_total += peso*expresión
    
    penalizaciones['total'] = penalización_total

    return penalizaciones


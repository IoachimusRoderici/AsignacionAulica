'''
En este módulo se definen las preferencias del sistema de asignación.

'''
from ortools.sat.python import cp_model
from pandas import DataFrame
from typing import Iterable

def obtener_cantidad_de_clases_fuera_del_edificio_preferido(modelo: cp_model.CpModel, clases: DataFrame, edificios: dict[str, Iterable[int]]):
    '''
    Agrega al modelo variables booleanas que representan si una clase está fuera de su edificio preferido.
    Devuelve la suma de esas variables, que representa la cantidad de clases fuera de su edificio preferido.

    :param modelo: Modelo que contiene las variables, restricciones, y penalizaciones.
    :param clases: Tabla con los datos de las clases.
    :param edificios: Diccionario de nombres de edificio a iterables de aulas.
    :return: La representación de la cantidad de clases fuera de su edificio preferido.
    '''

    cantidad_de_clases_fuera_del_edificio_preferido = 0

    for clase in clases.itertuples():

        aulas_del_edificio_preferido_en_un_formato_re_raro = [(aula,) for aula in edificios[clase.edificio_preferido]]

        # Definir flag de edificio preferido en el modelo
        fuera_del_edificio_preferido = modelo.new_bool_var(f"{clase.nombre}_fuera_del_edificio_preferido")
        modelo.add_allowed_assignments([clase.aula_asignada], aulas_del_edificio_preferido_en_un_formato_re_raro).only_enforce_if(~fuera_del_edificio_preferido)
        modelo.add_forbidden_assignments([clase.aula_asignada], aulas_del_edificio_preferido_en_un_formato_re_raro).only_enforce_if(fuera_del_edificio_preferido)

        cantidad_de_clases_fuera_del_edificio_preferido += fuera_del_edificio_preferido

    return cantidad_de_clases_fuera_del_edificio_preferido


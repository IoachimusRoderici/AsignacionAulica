'''
Funciones para analizar la asignación de aulas a posteriori.
'''
from pandas import DataFrame

def clases_con_aula_chica(clases: DataFrame, aulas: DataFrame, asignaciones: list[int]) -> set[int]:
    '''
    Devuelve un set con los índices de las clases que tienen aulas con capacidad
    menor a la cantidad de alumnos.
    '''
    clases_con_aula_chica = set()
    for i in clases.index:
        if clases.loc[i, 'cantidad_de_alumnos'] > aulas.loc[asignaciones[i], 'capacidad']:
            clases_con_aula_chica.add(i)
    
    return clases_con_aula_chica
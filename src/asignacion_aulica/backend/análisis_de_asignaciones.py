'''
Funciones para analizar la asignación de aulas a posteriori.
'''
from pandas import DataFrame

def clases_con_aula_chica(clases: DataFrame, aulas: DataFrame, asignaciones: list[int]) -> dict[int, int]:
    '''
    Devuelve un diccionario que mapea índices de clases a la cantidad de alumnos
    que no entran en el aula asignada a esa clase.

    Las clases que entran bien en sus aulas no son incluídas en el diccionario.
    '''
    clases_con_aula_chica = {}
    for i in clases.index:
        exceso = clases.loc[i, 'cantidad_de_alumnos'] - aulas.loc[asignaciones[i], 'capacidad']
        if exceso > 0:
            clases_con_aula_chica[i] = exceso
    
    return clases_con_aula_chica
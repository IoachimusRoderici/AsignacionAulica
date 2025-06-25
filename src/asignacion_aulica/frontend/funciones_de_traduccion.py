from pandas import DataFrame
import re
from asignacion_aulica.backend.dia import Día

def parsear_equipamiento(literal):
    componentes = (x.strip() for x in literal.split(','))
    return {componente for componente in componentes if componente != ''}

def horario_a_minutos(cadena):
    
    matches = re.findall(r'\d+', cadena) 
    if len(matches)==4:
        horario_inicio = int(matches[0])*60 + int(matches[1]) 
        horario_cierre = int(matches[2])*60 + int(matches[3])
        return horario_inicio, horario_cierre




def construir_diccionario_de_horarios(aula):
    """aula es un named tuple de dataframe, que tiene como atributos los solicitados en los ifs
    """
    horarios = {}
    if aula.Lunes != "CERRADO":
        horarios[Día.LUNES] = horario_a_minutos(aula.Lunes)
    if aula.Martes != "CERRADO":
        horarios[Día.MARTES] = horario_a_minutos(aula.Martes)
    if aula.Miércoles != "CERRADO":
        horarios[Día.MIÉRCOLES] = horario_a_minutos(aula.Miercoles)
    if aula.Jueves != "CERRADO":
        horarios[Día.JUEVES] = horario_a_minutos(aula.Jueves)
    if aula.Viernes != "CERRADO":
        horarios[Día.VIERNES] = horario_a_minutos(aula.Viernes)
    if aula.Sábado != "CERRADO":
        horarios[Día.SÁBADO] = horario_a_minutos(aula.Sábado)
    if aula.Domingo != "CERRADO":
        horarios[Día.DOMINGO] = horario_a_minutos(aula.Domingo)
    return horarios


def traducir_aulas(aulas_frontend:DataFrame):
    aulas_backend = DataFrame()
    aulas_backend['nombre'] = aulas_frontend['Aula']
    aulas_backend['edificio'] = aulas_frontend['Edificio']
    aulas_backend['capacidad'] = aulas_frontend['Capacidad']
    aulas_backend['equipamiento'] = list(map(parsear_equipamiento, aulas_frontend['equipamiento']))
    aulas_backend['horarios'] = list(map(construir_diccionario_de_horarios, aulas_frontend.itertuples()))
    return aulas_backend


"""
    :param clases: Tabla con los datos de todas las clases.
        Una clase por fila.
        Columnas:
        - nombre: str (materia y comisión)
        - día: Día
        - horario_inicio: int (medido en minutos)
        - horario_fin: int (medido en minutos)
        - cantidad_de_alumnos: int
        - equipamiento_necesario: set[str]
        - edificio_preferido: Optional[str]
        - aula_asignada: Optional[int]"""



#def traducir_actividades_a_clases(materias_frontend:DataFrame):
    



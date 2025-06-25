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

def horario_simple_a_minutos(cadena):
    
    matches = re.findall(r'\d+', cadena) 
    if len(matches)==2:
        horario_inicio = int(matches[0])*60 + int(matches[1])
        return horario_inicio


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



def traducir_clases(clases_frontend:DataFrame):
    """Metodo para traducir un dataframe de clases de frontend, al necesario para backend"""
    mapeador_de_dias = {'Lunes':Día.LUNES ,
                        'Martes':Día.MARTES,
                        'Miércoles':Día.MIÉRCOLES,
                        'Jueves':Día.JUEVES,
                        'Viernes':Día.VIERNES,
                        'Sábado':Día.SÁBADO,
                        'Domingo':Día.DOMINGO   }
    
    clases_backend = DataFrame()        
    clases_backend['nombre'] = clases_frontend['Nombre']
    clases_backend['día'] = mapeador_de_dias[clases_frontend['Día']]
    clases_backend['horario_inicio']        =   horario_simple_a_minutos(clases_frontend['Horario de inicio'])
    clases_backend['horario_fin']           =   horario_simple_a_minutos(clases_frontend['Horario de fin'])
    clases_backend['cantidad_de_alumnos']   =   clases_frontend['Cantidad de alumnos']
    clases_backend['equipamiento_necesario']=   list(map(parsear_equipamiento, clases_frontend['Equipamiento necesario']))
    clases_backend['edificio_preferido']    =   clases_frontend['Edificio preferencial']
    clases_backend['aula_asignada']         =   clases_frontend['Aula asignada']


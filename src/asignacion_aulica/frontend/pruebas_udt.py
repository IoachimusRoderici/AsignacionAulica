# -*- coding: utf-8 -*-

from datetime import datetime, time, timedelta
from typing import List
from udt import *

###############################################################################

# === ORDEN DE CONFIGURACIÓN ===
# 1) Universidad
# Universidad <- Edificios, Carreras, Actividades (o materias)
# -> Se crea la universidad para almacenar cada edificio
# 2) Edificios
# Por cada Edificio <- Nombre, Horarios, Aulas
# -> Se crea el edificio y se lo almacena en la Universidad
# -> Se asignan horarios de apertura y cierre por cada dia
# 3) Aulas y Equipamiento
# Por cada Aula <- Identificador, Capacidad, Equipamiento, Horario
# Por cada Equipamiento <- Objetos
# Por cada Objeto <- Nombre, Cantidad
# -> Se crean los objetos necesarios para el equipamiento de un aula
# -> Se crean los equipamientos (almacenan los objetos) de un aula
# -> Se crean los horarios de un aula (por defecto se usaría el horario del edificio)
# -> Se almacena el aula en el edificio correspondiente
# 4) Carreras
# Por cada Carrera <- Nombre, Edificio de preferencia
# -> Se crea la carrera y se la almacena en la Universidad
# 5) Actividades o Materias
# Por cada Actividad <- Identificador, Nombre, Comisión, Horarios (opc, determinado por algoritmo), Carrera (opc), Año, Cantidad de alumnos, Equipamiento
# -> Se crea la Actividad (o materia) con su identificador, nombre y comisión (puede ser None)
# -> Opcionalmente se puede asignar manualmente el horario
# -> Se asignan los otros datos necesarios
# -> Se almacena en la Universidad

# El programa debería asignar aulas y horarios automáticamente mediante la
# acción del algoritmo. Si es necesario o preferido, se puede asignar
# manualmente los horarios de cada Actividad.

# Si a un Aula no se le asigna un horario en la que estaría disponible,
# entonces por defecto se le asignará el horario del Edificio correspondiente.
# Por eso es importante primero crear el Edificio con su horario ya definido, y
# luego crear el Aula y asignarle el horario, o dejar que se asigne por
# defecto.


###############################################################################

# Configuración de prueba

# 1) Universidad
# ============================

# Se crea/instancia la Universidad.
UNRN_SA = Universidad()

# Se crean los edificios con los que cuenta la Universidad (los nombres).
Anasagasti: str = "Anasagasti 2"
Mitre: str = "Mitre 630"

# Se los almacena en la Unviersidad.
UNRN_SA.crear_edificio(Anasagasti)
UNRN_SA.crear_edificio(Mitre)

# Se imprimen los edificios creados con toda su información disponible.
print("Se crean edificios Anasagasti y Mitre:")
print("----------------------------------------------------------------------")
print(UNRN_SA.imprimir_edificio())
print("----------------------------------------------------------------------\n")

# 2) Edificios
# ============================

# Se crean los horarios de los edificios.
apertura:   datetime.time = time(8, 0)  # 08:00 hs
cierre:     datetime.time = time(22, 0) # 22:00 hs

lunes:      Horario = Horario(Dia.LUNES, apertura, cierre)      # Lunes de 08:00 hs a 22:00 hs
martes:     Horario = Horario(Dia.MARTES, apertura, cierre)     # Martes de 08:00 hs a 22:00 hs
miercoles:  Horario = Horario(Dia.MIERCOLES, apertura, cierre)  # Miércoles de 08:00 hs a 22:00 hs
jueves:     Horario = Horario(Dia.JUEVES, apertura, cierre)     # Jueves de 08:00 hs a 22:00 hs
viernes:    Horario = Horario(Dia.VIERNES, apertura, cierre)    # Viernes de 08:00 hs a 22:00 hs
sabado:     Horario = Horario(Dia.SABADO, apertura, cierre)     # Sábado de 08:00 hs a 22:00 hs

# Se asignan los horarios al edificio de Anasagasti.
Horarios_Anasagasti: List[Horario] = [lunes, martes, miercoles, jueves, viernes, sabado]
for horario in Horarios_Anasagasti:
    UNRN_SA.edificio(Anasagasti).asignar_horario(horario)

# Se asignan los horarios al edificio de Mitre.
UNRN_SA.edificio(Mitre).agregar_horario(Dia.LUNES, apertura, cierre)
UNRN_SA.edificio(Mitre).agregar_horario(Dia.MARTES, apertura, cierre)
UNRN_SA.edificio(Mitre).agregar_horario(Dia.MIERCOLES, apertura, cierre)
UNRN_SA.edificio(Mitre).agregar_horario(Dia.JUEVES, apertura, cierre)
UNRN_SA.edificio(Mitre).agregar_horario(Dia.VIERNES, apertura, cierre)
    
# Se imprimen los edificios creados con toda su información.
# (ahora incluye el horario)
print("Se asignan los horarios a los edificios:")
print("----------------------------------------------------------------------")
print(UNRN_SA.imprimir_edificios())
print("----------------------------------------------------------------------\n")

# 3) Aulas y Equipamiento
# ============================

# Se crean los objetos. (opcionalmente se puede indicar cantidad)
pizarron:   Objeto = Objeto("Pizarron") # Pizarrón de tiza
pizarra:    Objeto = Objeto("Pizarra") # Pizarra de marcador
proyector:  Objeto = Objeto("Proyector")
marcadores: Objeto = Objeto("Marcadores", 5)

# Se crea el equipamiento para algún aula.
equipamiento: Equipamiento = Equipamiento([pizarron, pizarra, proyector])

# Se crean aulas.
aula_b201: Aula = Aula("B201", capacidad=50, equipamiento=equipamiento)
aula_b202: Aula = Aula("B202")
aula_b202.asignar_equipamiento(equipamiento)
aula_b202.agregar_objeto(marcadores)

# Se agregan las aulas al edificio de la universidad.
UNRN_SA.edificio(Anasagasti).agregar_aula(aula_b201)
UNRN_SA.edificio(Anasagasti).agregar_aula(aula_b202)
UNRN_SA.crear_aula(Anasagasti, "B203")

# Se imprime la información de cada aula.
print("Se crean aulas:")
print("----------------------------------------------------------------------")
print(UNRN_SA.imprimir_aulas())
print("----------------------------------------------------------------------\n")

# 4) Carreras
# ============================

# Se crean las carreras de la Universidad.
ing_comp: Carrera = Carrera("Ingenieria en Computacion", preferencia=UNRN_SA.edificio(Anasagasti))
ing_elec: Carrera = Carrera("Ingenieria Electronica")
lic_econ: Carrera = Carrera("Licenciatura en Economía")

# Se las almacena en la Universidad.
UNRN_SA.agregar_carrera(ing_comp)
UNRN_SA.agregar_carrera(ing_elec)
UNRN_SA.agregar_carrera(lic_econ)
UNRN_SA.crear_carrera("Tecnicatura en Viveros", Anasagasti)

# Se imprime la información de cada carrera.
print("Se crean carreras:")
print("----------------------------------------------------------------------")
print(UNRN_SA.imprimir_carreras())
print("----------------------------------------------------------------------\n")


# 5) Actividades o Materias
# ============================

# Se crean materias.
progra1_A: Actividad = Actividad("ICOMP-PI", "Programacion I", comision="A", carrera=ing_comp)
progra1_B: Actividad = Actividad("ICOMP-PI", "Programacion I", comision="B")
progra2:   Actividad = Actividad("ICOMP-PII", "Programacion II", comision=None, carrera=ing_comp)
matematica:Actividad = Actividad("LE-M", "Matematica", comision=None)

progra1_B.asignar_carrera(ing_comp)

# Se las almacena en la Universidad.
UNRN_SA.agregar_actividad(progra1_A)
UNRN_SA.agregar_actividad(progra1_B)
UNRN_SA.agregar_actividad(progra2)
UNRN_SA.agregar_actividad(matematica)

UNRN_SA.actividad("ICOMP-PI", "Programacion I", "B").asignar_carrera(ing_comp)
UNRN_SA.actividad("LE-M", "Matematica", comision=None).asignar_carrera(lic_econ)

# Se imprime la información de cada actividad.
print("Se crean actividades:")
print("----------------------------------------------------------------------")
print(UNRN_SA.imprimir_actividades())
print("----------------------------------------------------------------------\n")


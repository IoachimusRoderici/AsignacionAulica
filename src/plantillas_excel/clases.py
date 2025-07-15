'''
Este script crea la plantilla para el archivo excel de clases/horarios/aulas.

La plantilla está basada en el archivo excel que les directores de carreras le
pasan al encargado de la asignación. Se modificaron algunas cosas para que sea
más usable.

La plantilla tiene un preámbulo que consiste de:
- El logo de la universidad
- El nombre de la carrera
- El año y número de cuatrimestre

Abajo del preámbulo hay una tabla con las siguientes columnas:
- Año
- Materia
- Cuatrimestral / Anual
- Comisión
- Teórica / Práctica
- Cupo
- Día de la semana
- Horario de inicio
- Horario de fin
- Docente
- Auxiliar
- Promocionable (Si (nota) / No)
- Lugar
- Aula

La tabla tiene una fila de la tabla por cada clase, con celdas unidas
verticalmente (por ejemplo, la columna "Materia" está unida en las filas de las
clases de cada materia).
'''
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.worksheet.table import Table
from openpyxl.drawing.image import Image
from openpyxl import Workbook

import sys

from estilos import (
    insertar_logo,
    fill_rojo_unrn,
    font_default,
    font_preámbulo_grande,
    font_preámbulo_chica,
    font_table_header,
    centrado,
    a_la_derecha,
    a_la_izquierda
)

COLUMNAS = (
    'Año',
    'Materia',
    'Cuatrimestral / Anual',
    'Comisión',
    'Teórica / Práctica',
    'Cupo',
    'Dia',
    'Horario de inicio',
    'Horario de fin',
    'Docente',
    'Auxiliar',
    'Promocionable',
    'Lugar',
    'Aula'
)

def insertar_logo(hoja: Worksheet):
    imagen = Image(logo_path)
    scale_ratio = points_to_pixels(logo_height) / imagen.height
    imagen.height *= scale_ratio
    imagen.width *= scale_ratio

    hoja.add_image(imagen, 'A1')
    hoja.row_dimensions[1].height = pixels_to_points(imagen.height) + 1

    hoja.merge_cells('A1:N1')

def agregar_preámbulo(hoja: Worksheet):
    for fila in FILAS_PREÁMBULO:
        hoja.append(fila)
        hoja.append(())
    
    hoja['A2'].font = font_preámbulo
    hoja['A2'].fill = fill_preámbulo

def agregar_tabla(hoja: Worksheet):
    hoja.append(COLUMNAS)
    hoja.append((
        '2025',
        'programación',
        'Cuatrimestral',
        'com1',
        'Teórica',
        25,
        'Lunes',
        '17:00',
        '20:00',
        'M. Vilugron',
        'D. Teira',
        'Si (8)',
        'Anasagasti 2',
        'B103'
    ))
    tabla = Table(displayName='Datos', ref='A6:N15')
    hoja.add_table(tabla)

def crear_plantilla() -> Workbook:
    plantilla = Workbook()
    hoja = plantilla.active
    hoja.title = 'Plantilla'
    
    insertar_logo(hoja)
    agregar_preámbulo(hoja)
    agregar_tabla(hoja)

    return plantilla

def main():
    plantilla = crear_plantilla()
    plantilla.save(sys.argv[1])

if __name__ == '__main__':
    main()

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
from openpyxl.utils.units import pixels_to_points, points_to_pixels
from openpyxl.drawing.image import Image
from openpyxl import Workbook, worksheet
from os import path
import sys

este_directorio = path.split(__file__)[0]

logo_path = path.join(este_directorio, 'unrn_logo.png')
logo_height = 50 #pts

FILAS_PREÁMBULO = (
    ('Universidad Nacional de Río Negro',),
    ('Carrera:', None),
    ('Año:', None, 'Cuatrimestre:', None)
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

def insertar_logo(hoja: worksheet):
    imagen = Image(logo_path)
    scale_ratio = points_to_pixels(logo_height) / imagen.height
    imagen.height *= scale_ratio
    imagen.width *= scale_ratio

    hoja.add_image(imagen, 'A1')
    hoja.row_dimensions[1].height = pixels_to_points(imagen.height) + 1

    hoja.merge_cells('A1:R1')

def agregar_preámbulo(hoja: worksheet):
    for fila in FILAS_PREÁMBULO:
        hoja.append(fila)
        hoja.append(())

def agregar_tabla(hoja: worksheet):
    hoja.append(COLUMNAS)
    hoja.append(())

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

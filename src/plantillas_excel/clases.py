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
from openpyxl.utils.cell import get_column_letter
from openpyxl.worksheet.table import Table
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

from validadores import (
    no_cambiar_este_valor,
    año_del_plan_de_estudios,
    número_natural,
    día_de_la_semana,
    horario
)

COLUMNAS = (
    'Año',
    'Materia',
    'Cuatrimestral / Anual',
    'Comisión',
    'Teórica / Práctica',
    'Cupo',
    'Día',
    'Horario inicio',
    'Horario fin',
    'Docente',
    'Auxiliar',
    'Promociona\nSi (Nota) / No',
    'Lugar',
    'Aula'
)

n_columns = len(COLUMNAS)
max_column = get_column_letter(n_columns)

def insertar_preámbulo(hoja: Worksheet):
    # Logo
    insertar_logo(hoja)
    hoja.merge_cells(start_row=1, end_row=1, start_column=1, end_column=n_columns)
    no_cambiar_este_valor.add(f'A1:{max_column}1')

    # Carrera
    fila = 2
    hoja.row_dimensions[fila].height = font_preámbulo_grande.size + 7

    hoja.merge_cells(start_row=fila, end_row=fila, start_column=1, end_column=2)
    cell = hoja.cell(fila, 1, value='Carrera: ')
    cell.fill = fill_rojo_unrn
    cell.font = font_preámbulo_grande
    cell.alignment = a_la_derecha
    no_cambiar_este_valor.add(f'A{fila}:B{fila}')

    hoja.merge_cells(start_row=fila, end_row=fila, start_column=3, end_column=n_columns)
    cell = hoja.cell(fila, 3, value='')
    cell.fill = fill_rojo_unrn
    cell.font = font_preámbulo_grande
    cell.alignment = a_la_izquierda
    no_cambiar_este_valor.add(f'A{fila+1}:{max_column}{fila+1}')
    hoja.merge_cells(start_row=fila+1, end_row=fila+1, start_column=1, end_column=n_columns)

    # Año y cuatrimestre
    fila += 2
    hoja.row_dimensions[fila].height = font_preámbulo_chica.size + 7

    hoja.merge_cells(start_row=fila, end_row=fila, start_column=1, end_column=2)
    cell = hoja.cell(fila, 1, value='Año: ')
    cell.fill = fill_rojo_unrn
    cell.font = font_preámbulo_chica
    cell.alignment = a_la_derecha
    no_cambiar_este_valor.add(f'A{fila}:B{fila}')

    cell = hoja.cell(fila, 3, value='') # Celda para completar el año
    cell.fill = fill_rojo_unrn
    cell.font = font_preámbulo_chica
    cell.alignment = a_la_izquierda

    hoja.merge_cells(start_row=fila, end_row=fila, start_column=4, end_column=5)
    cell = hoja.cell(fila, 4, value='Cuatrimestre: ')
    cell.fill = fill_rojo_unrn
    cell.font = font_preámbulo_chica
    cell.alignment = a_la_derecha
    no_cambiar_este_valor.add(f'D{fila}:E{fila}')

    hoja.merge_cells(start_row=fila, end_row=fila, start_column=6, end_column=n_columns)
    cell = hoja.cell(fila, 6, value='') # Celda para completar el cuatrimestre
    cell.fill = fill_rojo_unrn
    cell.font = font_preámbulo_chica
    cell.alignment = a_la_izquierda
    hoja.merge_cells(start_row=fila+1, end_row=fila+1, start_column=1, end_column=n_columns)
    no_cambiar_este_valor.add(f'A{fila+1}:{max_column}{fila+1}')

def insertar_tabla(hoja: Worksheet):
    # Intertar fila con los nombres de las columnas
    hoja.append(COLUMNAS)
    fila_header = hoja.max_row
    no_cambiar_este_valor.add(f'A{fila_header}:{max_column}{fila_header}')

    # Configurar estilo de los nombres
    for i in range(1, n_columns+1):
        cell = hoja.cell(fila_header, i)
        cell.font = font_table_header
        cell.alignment = centrado
    
    # Ajustar tamaños de las columnas
    font_size_ratio = font_table_header.size / 11
    hoja.column_dimensions['A'].width =  5 * font_size_ratio # Año
    hoja.column_dimensions['B'].width = 25 * font_size_ratio # Materia
    hoja.column_dimensions['C'].width = 12 * font_size_ratio # Cuatrimestral o anual
    hoja.column_dimensions['D'].width =  9 * font_size_ratio # Comisión
    hoja.column_dimensions['E'].width = 10 * font_size_ratio # Teórica o práctica
    hoja.column_dimensions['F'].width =  5 * font_size_ratio # Cupo
    hoja.column_dimensions['G'].width =  8 * font_size_ratio # Día
    hoja.column_dimensions['H'].width =  7 * font_size_ratio # Horario de inicio
    hoja.column_dimensions['I'].width =  7 * font_size_ratio # Horario de fin
    hoja.column_dimensions['J'].width = 12 * font_size_ratio # Docente
    hoja.column_dimensions['K'].width = 12 * font_size_ratio # Auxiliar
    hoja.column_dimensions['L'].width = 14 * font_size_ratio # Promocionable
    hoja.column_dimensions['M'].width = 12 * font_size_ratio # Lugar
    hoja.column_dimensions['N'].width =  8 * font_size_ratio # Aula

    # Agregar validadores
    año_del_plan_de_estudios.add(f'A{fila_header+1}:A1048576') # 1048576 significa hasta el final de la columna.
    número_natural.add(f'F{fila_header+1}:F1048576') # Cupo 
    día_de_la_semana.add(f'G{fila_header+1}:G1048576') # Día
    horario.add(f'H{fila_header+1}:H1048576') # Horario de inicio
    horario.add(f'I{fila_header+1}:I1048576') # Horario de fin

def crear_plantilla() -> Workbook:
    plantilla = Workbook()
    plantilla._fonts[0] = font_default

    hoja = plantilla.active
    hoja.title = 'Plantilla'
    hoja.add_data_validation(no_cambiar_este_valor)
    hoja.add_data_validation(año_del_plan_de_estudios)
    hoja.add_data_validation(número_natural)
    hoja.add_data_validation(día_de_la_semana)
    hoja.add_data_validation(horario)
    
    insertar_preámbulo(hoja)
    insertar_tabla(hoja)

    return plantilla

def main():
    plantilla = crear_plantilla()
    plantilla.save(sys.argv[1])

if __name__ == '__main__':
    main()

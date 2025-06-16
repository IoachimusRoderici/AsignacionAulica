# -*- coding: utf-8 -*-
"""
Apartado de configuración para el input y output de datos de las Actividades/
Materias de la Universidad.

@author: Cristian
"""

import flet as ft
from pandas import DataFrame

from typing import List

from datos import *
#from config import UI_Config


class UI_Config_Actividades():
    """
    Apartado de Actividades/Materias de la universidad.
    """
    def __init__(
            self
            ):
        """
        Crea el apartado de aulas de los edificios la universidad.
        
        Layout (por filas):
        -----------------------------------------------------------------------
        0) Título: "Configuración de Actividades/Materias de la Universidad"
        1) Dropdown identificador - Drop. nombre actividad - Drop. comisión - Botón eliminar actividad
        2) Campo nombre de carrera - Btn. agregar carrera - Btn. modificar carrera
        3) Drop. edificio preferido para la carrera - Btn. eliminar preferencia
        4) ----- (linea divisora) -----
        5) Tabla con datos de las carreras

        Returns
        -------
        None.

        """
        
        self.fila: List[ft.Row] = []
        
        # Fila 0:
        # 0) Título: "Configuración de Actividades/Materias de la Universidad"
        self.titulo = ft.Text(
            "Configuración de Actividades/Materias de la Universidad",
            size=20,
            selectable=False
        )
        
        # Fila 1:
        # 1) Dropdown identificador - Drop. nombre actividad - Drop. comisión - Botón eliminar actividad
        self.lista_identificador_actividades = ft.Dropdown(
            label="Identificador"
        )
        self.lista_nombre_actividades = ft.Dropdown(
            label="Nombre de actividad"
        )
        
        # Fila 2:
        # 2) Campo nombre de carrera - Btn. agregar carrera - Btn. modificar carrera
        self.lista_comision_actividades = ft.Dropdown(
            label="Comisión"
        )
        self.boton_eliminar_actividad = ft.Button(
            "Eliminar actividad"
        )
        
        # Fila 3:
        # 3) Drop. edificio preferido para la carrera - Btn. eliminar preferencia
        self.campo_identificador_actividad = ft.TextField(
            label="Identificador"
        )
        self.campo_nombre_actividad = ft.TextField(
            label="Nombre de actividad"
        )
        
        # Fila 4:
        # 4) ----- (linea divisora) -----
        self.campo_comision_actividad = ft.TextField(
            label="Comisión"
        )
        self.boton_agregar_actividad = ft.Button(
            "Agregar actividad"
        )
        self.boton_modificar_actividad = ft.Button(
            "Modificar actividad"
        )
        
        # Fila 5:
        # 5) Tabla con datos de las carreras
        self.tabla = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Identificador")),
                ft.DataColumn(ft.Text("Nombre")),
                ft.DataColumn(ft.Text("Comisión")),
                ft.DataColumn(ft.Text("Carrera")),
                ft.DataColumn(ft.Text("Año")),
                ft.DataColumn(ft.Text("Cant. de Alumnos")),
                ft.DataColumn(ft.Text("Preferencia Edificio"))
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("PI")),
                        ft.DataCell(ft.Text("Programación I")),
                        ft.DataCell(ft.Text("A")),
                        ft.DataCell(ft.Text("Ingeniería en Computación")),
                        ft.DataCell(ft.Text("1")),
                        ft.DataCell(ft.Text("100")),
                        ft.DataCell(ft.Text("Anasagasti")),
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("PI")),
                        ft.DataCell(ft.Text("Programación I")),
                        ft.DataCell(ft.Text("B")),
                        ft.DataCell(ft.Text("Ingeniería en Computación")),
                        ft.DataCell(ft.Text("1")),
                        ft.DataCell(ft.Text("100")),
                        ft.DataCell(ft.Text("Anasagasti")),
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("PII")),
                        ft.DataCell(ft.Text("Programación II")),
                        ft.DataCell(ft.Text("N/A")),
                        ft.DataCell(ft.Text("Ingeniería en Computación")),
                        ft.DataCell(ft.Text("2")),
                        ft.DataCell(ft.Text("100")),
                        ft.DataCell(ft.Text("Anasagasti")),
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Matemática I")),
                        ft.DataCell(ft.Text("MI")),
                        ft.DataCell(ft.Text("N/A")),
                        ft.DataCell(ft.Text("Ingeniería en Computación")),
                        ft.DataCell(ft.Text("1")),
                        ft.DataCell(ft.Text("50")),
                        ft.DataCell(ft.Text("Mitre")),
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Ingeniería de Software")),
                        ft.DataCell(ft.Text("IS")),
                        ft.DataCell(ft.Text("N/A")),
                        ft.DataCell(ft.Text("Ingeniería en Computación")),
                        ft.DataCell(ft.Text("4")),
                        ft.DataCell(ft.Text("50")),
                        ft.DataCell(ft.Text("Anasagasti")),
                    ]
                ),
            ],
        )
        
        self.fila.append(ft.Row([self.titulo]))
        self.fila.append(ft.Row([self.lista_identificador_actividades, self.lista_nombre_actividades]))
        self.fila.append(ft.Row([self.lista_comision_actividades, self.boton_eliminar_actividad]))
        self.fila.append(ft.Row([self.campo_identificador_actividad, self.campo_nombre_actividad]))
        self.fila.append(ft.Row([self.campo_comision_actividad, self.boton_agregar_actividad, self.boton_modificar_actividad]))
        self.fila.append(ft.Row([self.tabla]))
        
        # Columna final con todas las filas creadas.
        self.columna = ft.Column(
            controls=self.fila
        )
        self.container = ft.Container(
            content=self.columna
        )
    
    def dibujar(self) -> ft.Container:
        return self.container

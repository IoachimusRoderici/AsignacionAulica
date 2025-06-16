# -*- coding: utf-8 -*-
"""
Apartado de configuración para el input y output de datos de las Carreras de
la Universidad.

@author: Cristian
"""

import flet as ft
from pandas import DataFrame

from typing import List

from datos import *
#from config import UI_Config


class UI_Config_Carreras():
    """
    Apartado de Carreras de la universidad.
    """
    def __init__(
            self
            ):
        """
        Crea el apartado de aulas de los edificios la universidad.
        
        Layout (por filas):
        -----------------------------------------------------------------------
        0) Título: "Configuración de Carreras de la Universidad"
        1) Dropdown carreras - Botón eliminar carrera    
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
        # 0) Título: "Configuración de Carreras de la Universidad"
        self.titulo = ft.Text(
            "Configuración de Carreras de la Universidad",
            size=20,
            selectable=False
        )
        
        # Fila 1:
        # 1) Dropdown carreras - Botón eliminar carrera
        self.lista_carreras = ft.Dropdown(
            label="Carrera"
        )
        self.boton_eliminar_carrera = ft.Button(
            "Eliminar carrera"
        )
        
        # Fila 2:
        # 2) Campo nombre de carrera - Btn. agregar carrera - Btn. modificar carrera
        self.campo_nombre_carrera = ft.TextField(
            label="Nombre de la carrera"
        )
        self.boton_agregar_carrera = ft.Button(
            "Agregar carrera"
        )
        self.boton_modificar_carrera = ft.Button(
            "Modificar carrera"
        )
        
        # Fila 3:
        # 3) Drop. edificio preferido para la carrera - Btn. eliminar preferencia
        self.lista_edificios = ft.Dropdown(
            label="Edificio"
        )
        self.boton_eliminar_preferencia = ft.Button(
            "Eliminar preferencia de edificio"
        )
        
        # Fila 4:
        # 4) ----- (linea divisora) -----
        self.linea = ft.Divider(
            thickness=1
        )
        
        # Fila 5:
        # 5) Tabla con datos de las carreras
        self.tabla = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Carrera")),
                ft.DataColumn(ft.Text("Preferencia de Edificio"))
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Ingeniería en Computación")),
                        ft.DataCell(ft.Text("Anasagasti")),
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Ingeniería Electrónica")),
                        ft.DataCell(ft.Text("Anasagasti")),
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Antropología")),
                        ft.DataCell(ft.Text("Mitre")),
                    ]
                ),
            ],
        )
        
        self.fila.append(ft.Row([self.titulo]))
        self.fila.append(ft.Row([self.lista_carreras, self.boton_eliminar_carrera]))
        self.fila.append(ft.Row([self.campo_nombre_carrera, self.boton_agregar_carrera, self.boton_modificar_carrera]))
        self.fila.append(ft.Row([self.lista_edificios, self.boton_eliminar_preferencia]))
        self.fila.append(ft.Row([self.linea]))
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

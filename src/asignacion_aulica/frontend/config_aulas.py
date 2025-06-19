# -*- coding: utf-8 -*-
"""
Apartado de configuración para el input y output de datos de Aulas de los
Edificios de la Universidad.

@author: Cristian
"""

import flet as ft
from pandas import DataFrame

from typing import List

from .datos import *


class UI_Config_Aulas():
    """
    Apartado de Aulas de los Edificios de la universidad.
    """
    def __init__(
            self
            ):
        """
        Crea el apartado de aulas de los edificios la universidad.
        
        Layout (por filas):
        -----------------------------------------------------------------------
        0) Título: "Configuración de Aulas de los Edificios"
        1) Dropdown de edificios - Drop. de aulas - Botón eliminar aula
        2) Campo identificador aula - Campo capacidad aula - Btn. agregar aula - Btn. modificar aula
        3) ----- (linea divisora) -----
        4) Título: "Equipamiento del Aula"
        5) Drop. de equipamiento - Campo de nombre equipamiento - Btn. agregar equipamiento - Btn. eliminar eq.
        6) ----- (linea divisora) -----
        7) Título: "Horario del Aula"
        8) Drop. con día - Hora apertura - Hora cierre - Btn. establecer horario - Btn. eliminar horario
        9) ----- (linea divisora) -----
        10) Btn. mostrar aulas - Btn. mostrar eq. de aula
        11) Tabla con datos de los aulas

        Returns
        -------
        None.

        """
        
        self.fila: List[ft.Row] = []
        
        # Fila 0:
        # 0) Título: "Configuración de Aulas de los Edificios"
        self.titulo = ft.Text(
            "Configuración de Aulas de los Edificios",
            size=20,
            selectable=False
        )
        
        # Fila 1:
        # 1) Dropdown de edificios - Drop. de aulas - Botón eliminar aula
        self.lista_edificios = ft.Dropdown(
            label="Edificios"
        )
        self.lista_aulas = ft.Dropdown(
            label="Aulas"
        )
        self.boton_eliminar_aula = ft.Button(
            "Eliminar aula"
        )
        
        # Fila 2:
        # 2) Campo identificador aula - Campo capacidad aula - Btn. agregar aula - Btn. modificar aula
        self.campo_identificador_aula = ft.TextField(
            label="Identificador del aula"
        )
        self.campo_capacidad_aula = ft.TextField(
            label="Capacidad del aula"
        )
        self.boton_agregar_aula = ft.Button(
            "Agregar aula"
        )
        self.boton_modificar_aula = ft.Button(
            "Modificar aula"
        )
        
        # Fila 3:
        # 3) ----- (linea divisora) -----
        self.linea_0 = ft.Divider(
            thickness=1
        )
        
        # Fila 4:
        # 4) Título: "Equipamiento del Aula"
        self.titulo_equipamiento = ft.Text(
            "Equipamiento del Aula",
            size=20,
            selectable=False
        )
        
        
        # Fila 5:
        # 5) Drop. de equipamiento - Campo de nombre equipamiento - Btn. agregar equipamiento - Btn. eliminar eq.
        self.lista_equipamiento = ft.Dropdown(
            label="Equipamiento"
        )
        self.campo_equipamiento_aula = ft.TextField(
            label="Equipamiento del aula"
        )
        self.boton_agregar_equipamiento = ft.Button(
            "Agregar equipamiento"
        )
        self.boton_eliminar_equipamiento = ft.Button(
            "Eliminar equipamiento"
        )
        
        # Fila 6:
        # 6) ----- (linea divisora) -----
        self.linea_1 = ft.Divider(
            thickness=1
        )
        
        # Fila 7:
        # 7) Título: "Horario del Aula"
        self.titulo_horario = ft.Text(
            "Horario del Aula",
            size=20,
            selectable=False
        )
        
        # Fila 8:
        # 8) Drop. con día - Hora apertura - Hora cierre - Btn. establecer horario - Btn. eliminar horario
        self.lista_dias = ft.Dropdown(
            label="Día",
            options=[
                ft.dropdown.Option("Lunes"),
                ft.dropdown.Option("Martes"),
                ft.dropdown.Option("Miércoles"),
                ft.dropdown.Option("Jueves"),
                ft.dropdown.Option("Viernes"),
                ft.dropdown.Option("Sábado"),
                ft.dropdown.Option("Domingo")
            ],
            enable_filter=True,
        )
        self.lista_hora_apertura = ft.Dropdown(
            label="Hora",
            options=[
                ft.dropdown.Option(f"{i:02}") for i in range(24)
            ],
            enable_filter=True,
        )
        self.separador_0 = ft.Text(":")
        self.lista_minutos_apertura = ft.Dropdown(
            label="Minutos",
            options=[
                ft.dropdown.Option(f"{i:02}") for i in range(0, 60, 5)
            ],
            enable_filter=True,
        )
        self.separador_1 = ft.Text("-")
        self.lista_hora_cierre = ft.Dropdown(
            label="Hora",
            options=[
                ft.dropdown.Option(f"{i:02}") for i in range(24)
            ],
            enable_filter=True,
        )
        self.separador_2 = ft.Text(":")
        self.lista_minutos_cierre = ft.Dropdown(
            label="Minutos",
            options=[
                ft.dropdown.Option(f"{i:02}") for i in range(0, 60, 5)
            ],
            enable_filter=True,
        )
        self.boton_establecer_horario = ft.Button(
            text="Establecer horario",
        )
        self.boton_eliminar_horario = ft.Button(
            text="Eliminar horario",
        )
        
        # Fila 9:
        # 9) ----- (linea divisora) -----
        self.linea_2 = ft.Divider(
            thickness=1
        )
        
        # Fila 10:
        # 10) Btn. mostrar aulas - Btn. mostrar eq. de aula
        self.boton_mostrar_aulas = ft.Button(
            "Mostrar Aulas"
        )
        self.boton_mostrar_equipamiento_aulas = ft.Button(
            "Mostrar Equipamiento de Aula"
        )
        
        # Fila 11:
        # 11) Tabla con datos de los aulas
        self.tabla = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Edificio")),
                ft.DataColumn(ft.Text("Identificador de Aula")),
                ft.DataColumn(ft.Text("Capacidad")),
                ft.DataColumn(ft.Text("Lunes")),
                ft.DataColumn(ft.Text("Martes")),
                ft.DataColumn(ft.Text("Miércoles")),
                ft.DataColumn(ft.Text("Jueves")),
                ft.DataColumn(ft.Text("Viernes")),
                ft.DataColumn(ft.Text("Sábado")),
                ft.DataColumn(ft.Text("Domingo"))
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Anasagasti")),
                        ft.DataCell(ft.Text("B-101")),
                        ft.DataCell(ft.Text("50")),
                        ft.DataCell(ft.Text("9:00-21:00")),
                        ft.DataCell(ft.Text("9:00-21:00")),
                        ft.DataCell(ft.Text("9:00-21:00")),
                        ft.DataCell(ft.Text("9:00-21:00")),
                        ft.DataCell(ft.Text("9:00-21:00")),
                        ft.DataCell(ft.Text("9:00-21:00")),
                        ft.DataCell(ft.Text("CERRADO")),
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Anasagasti")),
                        ft.DataCell(ft.Text("B-201")),
                        ft.DataCell(ft.Text("50")),
                        ft.DataCell(ft.Text("9:00-21:00")),
                        ft.DataCell(ft.Text("9:00-21:00")),
                        ft.DataCell(ft.Text("9:00-21:00")),
                        ft.DataCell(ft.Text("9:00-21:00")),
                        ft.DataCell(ft.Text("9:00-21:00")),
                        ft.DataCell(ft.Text("9:00-21:00")),
                        ft.DataCell(ft.Text("CERRADO")),
                    ]
                )
            ],
        )
        
        self.fila.append(ft.Row([self.titulo]))
        self.fila.append(ft.Row([self.lista_edificios, self.lista_aulas, self.boton_eliminar_aula]))
        self.fila.append(ft.Row([self.campo_identificador_aula, self.campo_capacidad_aula, self.boton_agregar_aula, self.boton_modificar_aula]))
        self.fila.append(ft.Row([self.linea_0]))
        self.fila.append(ft.Row([self.titulo_equipamiento]))
        self.fila.append(ft.Row([self.lista_equipamiento, self.campo_equipamiento_aula, self.boton_agregar_equipamiento, self.boton_eliminar_equipamiento]))
        self.fila.append(ft.Row([self.linea_1]))
        self.fila.append(ft.Row([self.titulo_horario]))
        self.fila.append(ft.Row([self.lista_dias,
                                 self.lista_hora_apertura, self.separador_0, self.lista_minutos_apertura,
                                 self.separador_1,
                                 self.lista_hora_cierre, self.separador_2, self.lista_minutos_cierre,
                                 self.boton_establecer_horario,
                                 self.boton_eliminar_horario]))
        self.fila.append(ft.Row([self.linea_2]))
        self.fila.append(ft.Row([self.boton_mostrar_aulas, self.boton_mostrar_equipamiento_aulas]))
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

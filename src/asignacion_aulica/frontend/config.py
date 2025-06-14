# -*- coding: utf-8 -*-
"""
Apartados de configuración, inputs y outputs de datos. Incluye:
    - Edificios de la universidad
    - Aulas de los edificios
    - Carreras de la universidad
    - Actividades/materias de la universidad

@author: Cristian
"""

import flet as ft
from pandas import DataFrame

from typing import List
from colores import COLOR


class UI_BotonConfig():
    """
    Botón para cambiar de apartado. Por ejemplo: Edificios, Aulas, ...
    """
    def __init__(
            self,
            config_ref, # UI_Config
            texto: str, # Nombre del botón
            referencia: str # Referencia al nombre del apartado
            ):
        """
        Crea un botón para cambiar de apartado. Ejemplo de apartado: Edificios,
        Aulas, ...

        Parameters
        ----------
        config_ref : UI_Config
            Apartado o contenedor padre con todos los apartados hijos.
        texto : str
            Texto que llevará el botón. Ejemplo: "Edificios".
        referencia : str
            Referencia al nombre "clave" del apartado en cuestión.

        Returns
        -------
        None.

        """
        self.texto: str = texto
        self.config_ref = config_ref
        self.referencia = referencia
        self.tamanio_letra: int = 18
        self.tamanio_alto: int = 36
        
        self.texto_boton = ft.Text(
            value=self.texto,
            color=COLOR.BLANCO,
            text_align=ft.TextAlign.LEFT,
            size=self.tamanio_letra,
            selectable=False,
            )
        self.container_texto = ft.Container(
            content=self.texto_boton,
            alignment=ft.alignment.center_left,
            padding=ft.padding.symmetric(0, 20),
            )
        self.boton = ft.Container(
            content=self.container_texto,
            bgcolor=COLOR.ROJO,
            ink=True,
            on_click=lambda e: self.config_ref.cambiar_apartado(self.referencia), # llama a la función para cambiar de apartado de UI_Config
            height=self.tamanio_alto,
            border_radius=16,
            )
        
    def dibujar(self) -> ft.Container:
        return self.boton


class APARTADO():
    EDIFICIOS = "edificios"
    AULAS = "aulas"
    CARRERAS = "carreras"
    ACTIVIDADES = "actividades"
    HORARIOS = "horarios"

# APARTADOS:

class UI_Config_Edificios():
    """
    Apartado de Edificios de la universidad.
    """
    def __init__(
            self
            ):
        """
        Crea el apartado de edificios de la universidad.
        
        Layout (por filas):
        -----------------------------------------------------------------------
        0) Título: "Configuración de Edificios de la Universidad"
        1) Dropdown de edificios - Botón eliminar edificio
        2) Campo nombre edificio - Btn agregar edificio - Btn. modificar edificio
        3) ----- (linea divisora) -----
        4) Título: Horarios de apertura y cierre
        5) Drop. con día - Hora apertura - Hora cierre - Btn. agregar horario - Btn. eliminar horario
        6) ----- (linea divisora) -----
        7) Tabla con datos de los edificios cargados

        Returns
        -------
        None.

        """
        
        self.fila: List[ft.Row] = []
        
        # Fila 0:
        # Título
        self.titulo = ft.Text(
            value="Configuración de Edificios de la Universidad",
            text_align=ft.TextAlign.LEFT,
            size=20,
            selectable=False
        )
        self.fila.append(
            ft.Row(
                [
                    self.titulo
                ],
                alignment=ft.CrossAxisAlignment.END,
                expand=True,tight=False
            )
        )
        
        # Fila 1:
        # Dropdown de edificios - Botón eliminar edificio
        self.lista_edificios = ft.Dropdown(
            label="Edificios",
            options=[
                ft.dropdown.Option("Anasagasti"),
                ft.dropdown.Option("Mitre"),
            ],
            enable_filter=True,
            
        )
        self.boton_eliminar_edificio = ft.Button(
            text="Eliminar edificio",
        )
        self.fila.append(
            ft.Row(
                [
                    self.lista_edificios,
                    self.boton_eliminar_edificio
                ],
                scroll=ft.ScrollMode.ALWAYS,
            )
        )
        
        # Fila 2:
        # Campo nombre edificio - Btn agregar edificio - Btn. modificar edificio
        self.campo_nombre_edificio = ft.TextField(
            label="Nombre del edificio",
        )
        self.boton_agregar_edificio = ft.Button(
            text="Agregar edificio",
        )
        self.boton_modificar_edificio = ft.Button(
            text="Modificar edificio",
        )
        self.fila.append(
            ft.Row(
                [
                    self.campo_nombre_edificio,
                    self.boton_agregar_edificio,
                    self.boton_modificar_edificio
                ],
            )
        )
        
        # Fila 3: (línea divisora)
        # --------------------
        self.linea = ft.Divider(
            thickness=1
        )
        self.fila.append(
            ft.Row(
                [
                    self.linea
                ],
            )
        )
        
        # Fila 4:
        # Tabla con datos de los edificios cargados
        data = {
            "Nombre del Edificio": ["Anasagasti", "Mitre"],
            "Lunes": ["9:00-18:00", "9:00-18:00"],
            "Martes": ["12:00-21:00", "12:00-21:00"]
        }
        df = DataFrame(data)
        
        columnas = []
        filas = []
        
        for col_name in df:
            columnas.append(ft.DataColumn(ft.Text(col_name)))
            
        num_rows = df.shape[0]
        for i in range(num_rows):
            filas.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(df["Nombre del Edificio"].iloc[i])),
                    ft.DataCell(ft.Text(df["Lunes"].iloc[i])),
                    ft.DataCell(ft.Text(df["Martes"].iloc[i])),
                ]
            ))
        
        self.tabla = ft.DataTable(
            # columns=[
            #     ft.DataColumn(ft.Text("ID"), numeric=True),
            #     ft.DataColumn(ft.Text("Nombre del Edificio"))
            # ],
            # rows=[
            #     ft.DataRow(
            #         cells=[
            #             ft.DataCell(ft.Text("0")),
            #             ft.DataCell(ft.Text("Anasagasti"))
            #         ]
            #     ),
            #     ft.DataRow(
            #         cells=[
            #             ft.DataCell(ft.Text("1")),
            #             ft.DataCell(ft.Text("Mitre"))
            #         ]
            #     )
            # ]
            columns=columnas,
            rows=filas
        )
        self.fila.append(
            ft.Row(
                [
                    self.tabla
                ],
            )
        )
        
        # Columna final con todas las filas creadas.
        self.columna = ft.Column(
            controls=self.fila,
            alignment=ft.alignment.top_left,
        )
        self.container = ft.Container(
            content=self.columna,
            alignment=ft.alignment.top_left,
        )
    
    def dibujar(self) -> ft.Container:
        return self.container


class UI_Config_Aulas():
    """
    Apartado de Aulas de los Edificios de la universidad.
    """
    def __init__(
            self
            ):
        # Layout (por filas):
        # Título
        # Dropdown de edificios - Drop. de aulas - Botón eliminar aula
        # Campo identificador aula - Campo capacidad aula - Btn. agregar aula - Btn. modificar aula
        # --------------------
        # Drop. de equipamiento - Campo de nombre equipamiento - Btn. agregar equipamiento - Btn. eliminar eq.
        # --------------------
        # Btn. mostrar aulas - Btn. mostrar eq. de aula
        # Tabla con datos de los edificios/equip. por aula cargados
        
        self.fila: List[ft.Row] = []
        
        # Fila 0:
        # Título
        self.titulo = ft.Text(
            "Configuración de Aulas de los Edificios",
            size=20,
            selectable=False
        )
        self.fila.append(
            ft.Row(
                [
                    self.titulo
                ]
            )
        )
        
        # Fila 1:
        # Dropdown de edificios - Drop. de aulas - Botón eliminar aula
        self.lista_edificios = ft.Dropdown(
            label="Edificios"
        )
        self.lista_aulas = ft.Dropdown(
            label="Aulas"
        )
        self.boton_eliminar_aula = ft.Button(
            "Eliminar aula"
        )
        self.fila.append(
            ft.Row(
                [
                    self.lista_edificios,
                    self.lista_aulas,
                    self.boton_eliminar_aula
                ]
            )
        )
        
        # Fila 2:
        # Campo identificador aula - Campo capacidad aula - Btn. agregar aula - Btn. modificar aula
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
        self.fila.append(
            ft.Row(
                [
                    self.campo_identificador_aula,
                    self.campo_capacidad_aula,
                    self.boton_agregar_aula,
                    self.boton_modificar_aula
                ]
            )
        )
        
        # Fila 3: (linea divisora)
        # --------------------
        self.linea_0 = ft.Divider(
                thickness=1
            )
        self.fila.append(
            ft.Row(
                [
                    self.linea_0
                ]
            )
        )
        
        # Fila 4:
        # Drop. de equipamiento - Campo de nombre equipamiento - Btn. agregar equipamiento - Btn. eliminar eq.
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
        self.fila.append(
            ft.Row(
                [
                    self.lista_equipamiento,
                    self.campo_equipamiento_aula,
                    self.boton_agregar_equipamiento,
                    self.boton_eliminar_equipamiento
                ]
            )
        )
        
        # Fila 5: (linea divisora)
        # --------------------
        self.linea_1 = ft.Divider(
                thickness=1
            )
        self.fila.append(
            ft.Row(
                [
                    self.linea_1
                ]
            )
        )
        
        # Fila 6:
        # Btn. mostrar aulas - Btn. mostrar eq. de aula
        self.boton_mostrar_aulas = ft.Button(
                "Mostrar Aulas"
            )
        self.boton_mostrar_equipamiento_aulas = ft.Button(
                "Mostrar Equipamiento de Aula"
            )
        self.fila.append(
            ft.Row(
                [
                    self.boton_mostrar_aulas,
                    self.boton_mostrar_equipamiento_aulas
                ]
            )
        )
        
        # Fila 7:
        # Tabla con datos de los edificios/equip. por aula cargados
        self.tabla = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Edificio")),
                ft.DataColumn(ft.Text("Identificador de Aula")),
                ft.DataColumn(ft.Text("Capacidad"), numeric=True)
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Anasagasti")),
                        ft.DataCell(ft.Text("B-101")),
                        ft.DataCell(ft.Text("50"))
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Anasagasti")),
                        ft.DataCell(ft.Text("B-201")),
                        ft.DataCell(ft.Text("50"))
                    ]
                )
            ],
        )
        self.fila.append(
            ft.Row(
                [
                    self.tabla
                ]
            )
        )
        
        # Columna final con todas las filas creadas.
        self.columna = ft.Column(
            controls=self.fila
        )
        self.container = ft.Container(
            content=self.columna
        )
    
    def dibujar(self) -> ft.Container:
        return self.container


class UI_Config_Carreras():
    """
    Apartado de Carreras de la universidad.
    """
    def __init__(
            self
            ):
        self.titulo = ft.Text(
            "Configuración de Carreras de la Universidad",
            size=20,
            selectable=False
            )
        
        self.lista_carreras = ft.Dropdown(
            label="Carreras"
            )
        self.boton_eliminar_carrera = ft.Button(
            "Eliminar carrera"
            )
        self.fila_lista = ft.Row(
            [
                self.lista_carreras,
                self.boton_eliminar_carrera
            ]
            )
        
        self.campo_nombre_carrera = ft.TextField(
            label="Nombre de la carrera"
            )
        self.boton_agregar_carrera = ft.Button(
            "Agregar carrera"
            )
        self.fila_creacion = ft.Row(
            [
                self.campo_nombre_carrera,
                self.boton_agregar_carrera
            ]
            )
        
        self.lista_preferencia_edificio = ft.Dropdown(
            label="Edificio de preferencia"
            )
        
        self.columna = ft.Column(
            [
                self.titulo,
                self.fila_lista,
                self.fila_creacion,
                self.lista_preferencia_edificio
            ]
            )
        self.container = ft.Container(
            content=self.columna
            )
    
    def dibujar(self) -> ft.Container:
        return self.container


class UI_Config_Actividades():
    """
    Apartado de Actividades/Materias de la universidad.
    """
    def __init__(
            self
            ):
        self.titulo = ft.Text(
            "Configuración de Actividades/Materias de la Universidad",
            size=20,
            selectable=False
            )
        
        self.lista_identificador_actividades = ft.Dropdown(
            label="Identificador"
            )
        self.lista_nombre_actividades = ft.Dropdown(
            label="Nombre de actividad"
            )
        self.lista_comision_actividades = ft.Dropdown(
            label="Comisión"
            )
        self.boton_eliminar_actividad = ft.Button(
            "Eliminar actividad"
            )
        self.fila_lista = ft.Row(
            [
                self.lista_identificador_actividades,
                self.lista_nombre_actividades,
                self.lista_comision_actividades,
                self.boton_eliminar_actividad
            ]
            )
        
        self.campo_identificador_actividad = ft.TextField(
            label="Identificador"
            )
        self.campo_nombre_actividad = ft.TextField(
            label="Nombre de actividad"
            )
        self.campo_comision_actividad = ft.TextField(
            label="Comisión"
            )
        self.boton_agregar_actividad = ft.Button(
            "Agregar actividad"
            )
        self.fila_creacion = ft.Row(
            [
                self.campo_identificador_actividad,
                self.campo_nombre_actividad,
                self.campo_comision_actividad,
                self.boton_agregar_actividad
            ]
            )
        
        self.columna = ft.Column(
            [
                self.titulo,
                self.fila_lista,
                self.fila_creacion,
            ]
            )
        self.container = ft.Container(
            content=self.columna
            )
    
    def dibujar(self) -> ft.Container:
        return self.container

# MENU DE APARTADOS

class UI_Config():
    """
    Apartado 'Padre', con todos los apartados de la configuración.
    """
    def __init__(
            self,
            page: ft.Page
            ):
        self.page = page
        
        # Botones para configurar cada apartado.
        self.btn_edificios = UI_BotonConfig(self, "Edificios", APARTADO.EDIFICIOS)
        self.btn_aulas = UI_BotonConfig(self, "Aulas", APARTADO.AULAS)
        self.btn_carreras = UI_BotonConfig(self, "Carreras", APARTADO.CARRERAS)
        self.btn_actividades = UI_BotonConfig(self, "Actividades/materias", APARTADO.ACTIVIDADES)
        
        self.fila_botones = ft.Row(
            [
                self.btn_edificios.dibujar(),
                self.btn_aulas.dibujar(),
                self.btn_carreras.dibujar(),
                self.btn_actividades.dibujar()
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing = 10,
            scroll=ft.ScrollMode.AUTO,
            )
        
        self.apartado_edificios = UI_Config_Edificios()
        self.apartado_aulas = UI_Config_Aulas()
        self.apartado_carreras = UI_Config_Carreras()
        self.apartado_actividades = UI_Config_Actividades()
        
        self.apartado = self.apartado_edificios
        
        self.menu_config = ft.Column(
            [
                self.fila_botones,
                self.apartado.dibujar()
            ],
            alignment=ft.MainAxisAlignment.START,
            #expand=True
            )
        
        self.container = ft.Container(
            content=self.menu_config,
            alignment=ft.alignment.top_left,
            padding=20,
            expand=False,
            border=ft.border.all(1, "black")
        )
    
    def dibujar(self) -> ft.Container:
        return self.container
    
    def cambiar_apartado(self, apartado: str) -> None:
        """
        Cambia el apartado que se está mostrando actualmente.

        Parameters
        ----------
        apartado : str
            Palabra clave del nombre del apartado. Ejemplo: "edificios".

        Returns
        -------
        None.

        """
        match apartado:
            case APARTADO.EDIFICIOS:
                self.apartado = self.apartado_edificios
            case APARTADO.AULAS:
                self.apartado = self.apartado_aulas
            case APARTADO.CARRERAS:
                self.apartado = self.apartado_carreras
            case APARTADO.ACTIVIDADES:
                self.apartado = self.apartado_actividades
            case _:
                self.apartado = self.apartado_edificios
        self.menu_config.controls.clear()
        self.menu_config.controls.append(self.fila_botones)
        self.menu_config.controls.append(self.apartado.dibujar())
        self.menu_config.update()
        self.page.update()

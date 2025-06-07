# -*- coding: utf-8 -*-
"""
Created on Sat May 31 12:50:43 2025

@author: Cristian
"""

import flet as ft

from colores import COLOR


class UI_TituloConfig():
    def __init__(self, texto: str, icono: ft.Icon):
        pass
    
    def dibujar(self):
        return self.titulo


class UI_BotonConfig():
    def __init__(
            self,
            config_ref, # UI_Config
            texto: str, # Nombre del botón
            referencia: str # Referencia al nombre del apartado
            ):
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
            expand=False
            )
        self.container_texto = ft.Container(
            content=self.texto_boton,
            alignment=ft.alignment.center_left,
            padding=ft.padding.symmetric(0, 20),
            expand=False
            )
        self.boton = ft.Container(
            content=self.container_texto,
            bgcolor=COLOR.ROJO,
            ink=True,
            on_click=lambda e: self.config_ref.cambiar_apartado(self.referencia),
            height=self.tamanio_alto,
            border_radius=16,
            expand=False
            )
        
    def dibujar(self):
        return self.boton


class APARTADO():
    EDIFICIOS = "edificios"
    AULAS = "aulas"
    CARRERAS = "carreras"
    ACTIVIDADES = "actividades"

# APARTADOS

class UI_Config_Edificios():
    def __init__(
            self
            ):
        self.titulo = ft.Text(
            "Configuración de Edificios de la Universidad",
            size=20,
            selectable=False
            )
        
        self.lista_edificios = ft.Dropdown(
            label="Edificios"
            )
        self.boton_eliminar_edificio = ft.Button(
            "Eliminar edificio"
            )
        self.fila_lista = ft.Row(
            [
                self.lista_edificios,
                self.boton_eliminar_edificio
            ],
            scroll=ft.ScrollMode.ALWAYS
            )
        
        self.campo_nombre_edificio = ft.TextField(
            label="Nombre del edificio"
            )
        self.boton_agregar_edificio = ft.Button(
            "Agregar edificio"
            )
        self.fila_creacion = ft.Row(
            [
                self.campo_nombre_edificio,
                self.boton_agregar_edificio
            ]
            )
        
        self.columna = ft.Column(
            [
                self.titulo,
                self.fila_lista,
                self.fila_creacion
            ]
            )
        self.container = ft.Container(
            content=self.columna
            )
    
    def dibujar(self):
        return self.container


class UI_Config_Aulas():
    def __init__(
            self
            ):
        self.titulo = ft.Text(
            "Configuración de Aulas de los Edificios",
            size=20,
            selectable=False
            )
        
        self.lista_edificios = ft.Dropdown(
            label="Edificios"
            )
        
        self.lista_aulas = ft.Dropdown(
            label="Aulas"
            )
        self.boton_eliminar_aula = ft.Button(
            "Eliminar aula"
            )
        self.fila_lista = ft.Row(
            [
                self.lista_aulas,
                self.boton_eliminar_aula
            ]
            )
        
        self.campo_identificador_aula = ft.TextField(
            label="Identificador del aula"
            )
        self.campo_capacidad_aula = ft.TextField(
            label="Capacidad del aula"
            )
        self.boton_agregar_aula = ft.Button(
            "Agregar aula"
            )
        self.fila_creacion = ft.Row(
            [
                self.campo_identificador_aula,
                self.campo_capacidad_aula,
                self.boton_agregar_aula
            ]
            )
        
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
        self.fila_equipamiento = ft.Row(
            [
                self.lista_equipamiento,
                self.campo_equipamiento_aula,
                self.boton_agregar_equipamiento,
                self.boton_eliminar_equipamiento
            ]
            )
        
        self.columna = ft.Column(
            [
                self.titulo,
                self.lista_edificios,
                self.fila_lista,
                self.fila_creacion,
                ft.Divider(),
                self.fila_equipamiento
            ]
            )
        self.container = ft.Container(
            content=self.columna
            )
    
    def dibujar(self):
        return self.container


class UI_Config_Carreras():
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
    
    def dibujar(self):
        return self.container


class UI_Config_Actividades():
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
    
    def dibujar(self):
        return self.container

# MENU DE APARTADOS

class UI_Config():
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
            alignment=ft.CrossAxisAlignment.START,
            scroll=ft.ScrollMode.ALWAYS
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
            expand=True
            )
        
        self.container = ft.Container(
            self.menu_config,
            alignment=ft.alignment.top_left,
            padding=20,
            expand=True
            )
    
    def dibujar(self):
        return self.container
    
    def cambiar_apartado(self, apartado: str):
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

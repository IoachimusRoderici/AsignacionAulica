# -*- coding: utf-8 -*-
"""
Created on Tue May 20 20:54:47 2025

@author: Cristian
"""

import flet as ft

from .colores import COLOR
from .iconos import UI_Icono


class UI_UNRN:
    def __init__(self, ruta_imagen: str):
        # Directorio donde se encuentra la imágen del icono.
        # Ejemplo: "./ui/imgs/UNRN_Andina.png"
        self.ruta_imagen: str = ruta_imagen
        self.tamanio_imagen: int = 225
        self.tamanio_container: int = 250
        self.padding: int = self.tamanio_container - self.tamanio_imagen
        
        self.icono = ft.Image(
            src=self.ruta_imagen,
            width=self.tamanio_imagen,
            height=self.tamanio_imagen,
            fit=ft.ImageFit.CONTAIN
            )
        self.container = ft.Container(
            content=self.icono,
            alignment=ft.alignment.top_center,
            width=self.tamanio_container,
            height=self.tamanio_imagen,
            padding=ft.Padding(
                left=self.padding,
                top=0,
                right=self.padding,
                bottom=0
                )
            )

    def dibujar(self):
        return self.container


class UI_MenuBoton:
    def __init__(
            self,
            ruta_imagen: str,
            texto: str
            ):
        # Directorio donde se encuentra la imágen del icono del boton.
        # Ejemplo: "./ui/imgs/icono_menu.png"
        self.ruta_imagen: str = ruta_imagen
        # Texto que dirá el botón. Por ejemplo: "Menú"
        self.texto: str = texto
        
        self.padding_imagen: int = 14
        self.tamanio_letra: int = 24
        self.tamanio_imagen: int = 40
        self.tamanio_container_izq = (68, 68)
        self.tamanio_container_der = (182, 68)
        
        self.icono = ft.Image(
            src=self.ruta_imagen,
            height=self.tamanio_imagen, width=self.tamanio_imagen,
            fit=ft.ImageFit.CONTAIN
            )
        self.container_icono = ft.Container(
            content=self.icono,
            width=self.tamanio_container_izq[0],
            height=self.tamanio_container_izq[1],
            alignment=ft.alignment.center,
            expand=False
            )
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
            width=self.tamanio_container_der[0],
            height=self.tamanio_container_der[1],
            expand=False
            )
        
        self.boton = ft.Container(
            content=ft.Row([self.container_icono, self.container_texto]),
            bgcolor=COLOR.ROJO,
            ink=True,
            on_click=lambda e: print(f"Boton {self.texto} clickeado"),
            width=(self.tamanio_container_izq[0] + self.tamanio_container_der[0]),
            expand=False
            )
    
    def dibujar(self):
        return self.boton


class UI_Menu:
    def __init__(self):
        self.icono_UNRN = UI_UNRN("./imgs/UNRN_Andina.png")
        self.boton_menu = UI_MenuBoton("./imgs/icono_menu.png", "Menú")
        self.boton_nuevo = UI_MenuBoton("./imgs/icono_nuevo.png", "Nuevo")
        self.boton_abrir = UI_MenuBoton("./imgs/icono_abrir.png", "Abrir")
        self.boton_guardar = UI_MenuBoton("./imgs/icono_guardar.png", "Guardar")
        self.boton_importar = UI_MenuBoton("./imgs/icono_importar.png", "Importar")
        self.boton_exportar = UI_MenuBoton("./imgs/icono_exportar.png", "Exportar")
        
        self.subcolumna = ft.Column(
            [
                self.boton_menu.dibujar(),
                self.boton_nuevo.dibujar(),
                self.boton_abrir.dibujar(),
                self.boton_guardar.dibujar(),
                self.boton_importar.dibujar(),
                self.boton_exportar.dibujar()
            ],
            spacing=10,
            scroll=ft.ScrollMode.ALWAYS
            )
        
        self.columna = ft.Column(
            [
                self.icono_UNRN.dibujar(),
                self.subcolumna
            ],
            spacing=0,
            scroll=ft.ScrollMode.AUTO
            )
        
        self.container = ft.Container(
            self.columna,
            padding=0,
            bgcolor=COLOR.ROJO,
            expand=True
            )
    
    def dibujar(self):
        return self.container


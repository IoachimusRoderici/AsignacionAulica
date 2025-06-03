# -*- coding: utf-8 -*-
"""
Created on Wed May 28 12:50:21 2025

@author: Cristian
"""

import flet as ft


class UI_Icono():
    def __init__(self):
        self.TAMANIO: int = 40 # 40 px
        
        # Las rutas están escritas relativas al directorio padre, porque al
        # ejecutarse se instanciarán desde un archivo en esa carpeta. (De lo
        # contrario no funcionará)
        
        self.MENU = ft.Image(src="./ui/imgs/icono_menu.png",
                             height=self.TAMANIO,
                             width=self.TAMANIO,
                             fit=ft.ImageFit.CONTAIN)
        self.NUEVO = ft.Image(src="./ui/imgs/icono_nuevo.png",
                              height=self.TAMANIO,
                              width=self.TAMANIO,
                              fit=ft.ImageFit.CONTAIN)
        self.IMPORTAR = ft.Image(src="./ui/imgs/icono_importar.png",
                                 height=self.TAMANIO,
                                 width=self.TAMANIO,
                                 fit=ft.ImageFit.CONTAIN)
        self.ABRIR = ft.Image(src="./ui/imgs/icono_abrir.png",
                              height=self.TAMANIO,
                              width=self.TAMANIO,
                              fit=ft.ImageFit.CONTAIN)
        self.GUARDAR = ft.Image(src="./ui/imgs/icono_guardar.png",
                                height=self.TAMANIO,
                                width=self.TAMANIO,
                                fit=ft.ImageFit.CONTAIN)
        self.EXPORTAR = ft.Image(src="./ui/imgs/icono_exportar.png",
                                 height=self.TAMANIO,
                                 width=self.TAMANIO,
                                 fit=ft.ImageFit.CONTAIN)
        self.FLECHA_CLARA = ft.Image(src="./ui/imgs/icono_flecha_clara.png",
                                     height=self.TAMANIO,
                                     width=self.TAMANIO,
                                     fit=ft.ImageFit.CONTAIN)
        self.FLECHA_OSCURA = ft.Image(src="./ui/imgs/icono_flecha_oscura.png",
                                      height=self.TAMANIO,
                                      width=self.TAMANIO,
                                      fit=ft.ImageFit.CONTAIN)

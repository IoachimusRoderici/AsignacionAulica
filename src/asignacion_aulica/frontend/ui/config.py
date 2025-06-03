# -*- coding: utf-8 -*-
"""
Created on Sat May 31 12:50:43 2025

@author: Cristian
"""

import flet as ft


class UI_TituloConfig():
    def __init__(self, texto: str, icono: ft.Icon):
        pass
    
    def dibujar(self):
        return self.titulo


class UI_BotonConfig():
    def __init__(self):
        self.boton = ft.Button()
        
    def dibujar(self):
        return self.boton


class UI_Config():
    def __init__(self):
        self.menu_config = ft.Column(
            [ft.Text("HOLA")],
            expand=True
            )
        
        self.container = ft.Container(
            self.menu_config,
            padding=20,
            border=ft.border.all(2, "black"),
            expand=True
            )
    
    def dibujar(self):
        return self.container

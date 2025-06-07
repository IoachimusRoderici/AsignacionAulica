# -*- coding: utf-8 -*-
"""
Proyecto de Ingeniería de Software
Grupo Asignación Áulica
@author: Cristian
"""

import flet as ft

from colores import COLOR
from menu import UI_Menu
from config import UI_Config


def main(page: ft.Page):
    # Pagina principal
    page.title = "UNRN Andina - Asignación de Aulas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_width = 1280
    page.window_height = 720
    #page._set_attr("windowMinWidth", 1280)
    #page._set_attr("windowMinHeight", 720)
    page.expand = True
    
    # Fuente de la app
    page.fonts = {
        "Karla": "./fonts/Karla-Regular.ttf",
        "Open Sans": "./fonts/OpenSans-Regular.ttf",
        "Open Sans Condensed": "./fonts/OpenSans_Condensed-Regular.ttf"
    }
    page.theme = ft.Theme(font_family="Karla")  # Font de la App por default
    
    menu = UI_Menu()
    config = UI_Config(page)
    UI_Todo = ft.Row(
        [menu.dibujar(), config.dibujar()],
        spacing=0,
        scroll=ft.ScrollMode.ALWAYS,
        vertical_alignment=ft.CrossAxisAlignment.START,
        expand=True
        )
    
    page.add(UI_Todo)
    
    page.update()


if __name__ == "__main__":
    ft.app(main)

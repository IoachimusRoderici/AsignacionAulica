# -*- coding: utf-8 -*-
"""
Created on Wed May 21 12:48:45 2025

@author: Cristian
"""

import flet as ft

def main(page: ft.Page):
    # Pagina principal
    page.title = "UNRN Andina - Asignación de Aulas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_min_width = 1280
    page.window_min_height = 720
    page.window_width = 1280
    page.window_height = 720
    
    page.fonts = {
        "Karla": "./ui/fonts/Karla-Regular.ttf",
        "Open Sans": "./ui/fonts/OpenSans-Regular.ttf",
        "Open Sans Condensed": "./ui/fonts/OpenSans_Condensed-Regular.ttf"
    }

    page.theme = ft.Theme(font_family="Karla")  # Font de la App por default
    
    # ui_texto = ft.Text(value="Hola")
    # ui_menu = ft.Container(content=ui_texto,
    #                        bgcolor="#EB1C38",
    #                        expand=True)
    # page.add(ui_menu)
    
    # icono = ft.Image(
    #     src="./ui/imgs/icono_menu.png",
    #     height=40, width=40,
    #     fit=ft.ImageFit.CONTAIN
    #     )
    # container_icono = ft.Container(
    #     content=icono,
    #     padding=14,
    #     alignment=ft.alignment.center
    #     )
    # texto = ft.Text(
    #     value="Menú",
    #     color="#FFFFFF",
    #     text_align=ft.TextAlign.LEFT,
    #     size=24,
    #     selectable=False
    #     )
    # container_texto = ft.Container(
    #     content=texto,
    #     alignment=ft.alignment.center_left,
    #     height=68, width=182
    #     )
    # boton = ft.Container(
    #     content=ft.Row([container_icono, container_texto]),
    #     bgcolor="#EB1C38",
    #     ink=True,
    #     on_click=lambda e: print("Clickable with Ink clicked!"),
    #     width=250
    #     )
    # page.add(boton)
    
    columna1 = ft.Column([ft.Container(ft.Text("Col1"), width=250, bgcolor="red")])
    columna2 = ft.Column([columna1, ft.Container(ft.Text("Col2"), width=250, bgcolor="blue")])
    contenedor_izq = ft.Container(columna2, bgcolor="yellow", expand=True)
    
    columna3 = ft.Column([ft.Container(ft.Text("Col3"), bgcolor="green")])
    columna4 = ft.Column([columna3, ft.Container(ft.Text("Col4"), bgcolor="pink")])
    contenedor_der = ft.Container(columna4, bgcolor="orange", expand=True)
    
    fila = ft.Row([contenedor_izq, contenedor_der], expand=True)
    
    page.add(fila)


#ft.app(main)
if __name__ == "__main__":
    ft.app(main)
    #pandas dataframe
# -*- coding: utf-8 -*-
"""
Elementos de Alerta para el usuario (Interfaz de Usuario).

@author: Cristian
"""

import flet as ft


class VentanaAlerta():
    """
    Ventana de Alerta al Usuario, con mensaje y 1 botón para cerrar.
    """
    def __init__(
            self,
            page: ft.Page,
            mensaje_de_alerta: str
            ):
        """
        Al instanciarla abre automáticamente una ventana de alerta con un
        mensaje para el usuario. Posee un título con el contenido "Atención" y
        en el cuerpo de la ventana se encuentra el mensaje al usuario. Tiene un
        (1) botón para cerrarla.

        Parameters
        ----------
        page : ft.Page
            Page de la app para poder abrir la ventana de alerta.
        mensaje_de_alerta : str
            Mensaje a alertar al usuario. Por ejemplo: "Error con tipo de dato..."

        Returns
        -------
        None.

        """
        # Crea la ventana de alerta al usuario con el mensaje brindado.
        self.alerta = ft.AlertDialog(
            modal=True,
            title=ft.Text("Atención"),
            content=ft.Text(mensaje_de_alerta, selectable=True),
            actions=[
                ft.TextButton(
                    text="Aceptar",
                    on_click=lambda e: page.close(self.alerta)
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print(f"Alertado al usuario: {mensaje_de_alerta}"),
        )
        
        # Abre la alerta. (se cierra clickeando el botón del mensaje).
        page.open(self.alerta)

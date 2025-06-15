# -*- coding: utf-8 -*-
import re


def limpiar_texto(texto: str) -> str:
    """
    Limpia un texto o string de símbolos o espacios conflictivos que pudieran
    llegar a dar problema en el procesamiento de los datos.
    
    Quita los espacios antes y después del texto. Suprime los múltiples
    espacios a uno solo. Quita los símbolos problemáticos, a excepción del
    guión (-) y guión bajo (_).

    Parameters
    ----------
    texto : str
        Texto/string a limpiar. Por ejemplo: " h$o@la   soy   yo ".

    Returns
    -------
    str
        Texto/string limpio. Por ejemplo (usando el ejemplo del input): "hola soy yo".

    """
    # Se eliminan los caracteres que no sean letras, números, espacio, guión o
    # guión bajo.
    texto = re.sub(r"[^\w\s\-_]", "", texto)
    
    # Se eliminan los espacios al principio y al final.
    texto = texto.strip()

    # Se reemplazan los múltiples espacios por uno solo.
    texto = re.sub(r"\s+", " ", texto)

    return texto

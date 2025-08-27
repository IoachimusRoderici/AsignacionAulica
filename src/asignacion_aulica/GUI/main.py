from PySide6.QtGui import QGuiApplication, QFontDatabase, QIcon
from PySide6.QtQuickControls2 import QQuickStyle
from PySide6.QtQml import QQmlApplicationEngine
from pathlib import Path
import sys, os

from asignacion_aulica import assets

def configurar_fuente_por_defecto():
    for file in os.listdir(assets.get_path('fonts')):
        QFontDatabase.addApplicationFont(file)

    default_font = QFontDatabase.font('Karla', 'regular', 12)
    QGuiApplication.setFont(default_font)

def main() -> int:
    app = QGuiApplication(sys.argv)
    icono = QIcon(assets.get_path('iconos', 'unrn.ico'))
    app.setWindowIcon(icono)
    QQuickStyle.setStyle('Basic')

    configurar_fuente_por_defecto()

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty('assets_path', Path(assets.assets_path).as_uri())
    engine.addImportPath(assets.QML_path)
    engine.loadFromModule('QML', "Main")
    
    if engine.rootObjects():
        exit_code = app.exec()
    else:
        exit_code = -1

    del engine
    return exit_code

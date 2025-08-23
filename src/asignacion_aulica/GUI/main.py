import sys, os
from PySide6.QtGui import QGuiApplication, QFontDatabase
from PySide6.QtQml import QQmlApplicationEngine

from asignacion_aulica import assets

def configurar_fuente_por_defecto():
    default_font_file = assets.get_path('fonts', 'Karla-Regular.ttf')
    QFontDatabase.addApplicationFont(default_font_file)
    font = QFontDatabase.font('Karla', 'regular', 12)
    QGuiApplication.setFont(font)

def main() -> int:
    app = QGuiApplication(sys.argv)

    configurar_fuente_por_defecto()

    engine = QQmlApplicationEngine()
    engine.addImportPath(assets.QML_path)

    engine.loadFromModule('QML', "Main")
    
    if engine.rootObjects():
        exit_code = app.exec()
    else:
        exit_code = -1

    del engine
    return exit_code

if __name__ == '__main__':
    sys.exit(main())

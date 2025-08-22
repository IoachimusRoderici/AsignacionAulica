[app]
title = Asignación Áulica
icon = src/asignacion_aulica/assets/iconos/unrn.ico

# Dónde encontrar el código fuente
project_dir = src/asignacion_aulica
input_file = src/asignacion_aulica/main.py

# Dónde dejar el ejecutable
exec_directory = ./

project_file = # No usamos project file.

[python]
python_path = # Auto-detectar

# Si no ponemos esto, no funciona.
packages = Nuitka==2.6.8

[qt]
qml_files = asignacion_aulica/GUI/QML/Main.qml,asignacion_aulica/GUI/QML/BarraLateral/BarraLateral.qml,asignacion_aulica/GUI/QML/BarraLateral/BotónPestaña.qml,asignacion_aulica/GUI/QML/BarraLateral/Colores.qml
modules = Network,Qml,Gui,Core,DBus
plugins = platforms,networkaccess,platforms/darwin,xcbglintegrations,egldeviceintegrations,accessiblebridge,networkinformation,scenegraph,generic,imageformats,iconengines,tls,qmltooling,qmllint,platformthemes,platforminputcontexts
excluded_qml_plugins = QtCharts,QtQuick3D,QtSensors,QtTest,QtWebEngine

[nuitka]
macos.permissions = 

# mode of using nuitka. accepts standalone or onefile.
mode = onefile
extra_args = --quiet --noinclude-qt-translations --include-data-dir=assets=assets


# Este archivo configura el empaquetado de la aplicación.
# El empaquetador edita el archivo cada vez que se ejecuta.
# NO COMMITEAR LOS CAMBIOS QUE HACE EL EMPAQUETADOR.

[app]
title = Asignación Áulica
icon = assets/iconos/unrn.ico

# dónde encontrar el código fuente
project_dir = src/asignacion_aulica
input_file = src/asignacion_aulica/main.py

# dónde dejar el ejecutable
exec_directory = ./

project_file = # No usamos project file.

[python]
python_path = # Auto-detectar

# si no ponemos esto, no funciona.
packages = Nuitka==2.6.8

[qt]
qml_files = asignacion_aulica/GUI/QML/Main.qml,asignacion_aulica/GUI/QML/BarraLateral/BarraLateral.qml,asignacion_aulica/GUI/QML/BarraLateral/BotónPestaña.qml,asignacion_aulica/GUI/QML/BarraLateral/Colores.qml
modules = Qml,Network,Core,Gui,DBus
plugins = platforms,networkaccess,platforms/darwin,xcbglintegrations,egldeviceintegrations,accessiblebridge,networkinformation,scenegraph,generic,imageformats,iconengines,tls,qmltooling,qmllint,platformthemes,platforminputcontexts
excluded_qml_plugins = QtCharts,QtQuick3D,QtSensors,QtTest,QtWebEngine

[nuitka]
# generar un ejecutable de un solo archivo.
mode = onefile

# incluir assets en el archivo empaquetado.
extra_args = --quiet --noinclude-qt-translations --include-data-dir=assets=assets

# si no ponemos esto, no funciona
macos.permissions = 


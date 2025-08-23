; Configuración para generar el instalador con Inno Setup.
; Esta configuración se usa en el CI de GitHub.

[Setup]
AppName=Asignación Áulica
SetupIconFile=assets/iconos/unrn.ico

; Instalar en "Program Files" del usuario:
DefaultDirName={autopf}\AsignacionAulica

WizardStyle=modern

[Files]
Source: "build\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\Asignación Áulica"; Filename: "{app}\your_main_executable.exe"
Name: "{autodesktop}\Asignación Áulica"; Filename: "{app}\your_main_executable.exe"
Name: "{group}\Desinstalar Asignacion Áulica"; Filename: "{uninstallexe}"

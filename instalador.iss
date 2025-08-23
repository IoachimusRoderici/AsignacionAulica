; Configuración para generar el instalador con Inno Setup.
; Esta configuración se usa en el CI de GitHub.

[Setup]
AppName=Asignación Áulica
AppVersion=esto se completa en el CI
SetupIconFile=assets/iconos/unrn.ico
WizardStyle=modern

OutputDir=instalador

; Instalar en "Program Files" del usuario:
DefaultDirName={autopf}\AsignaciónÁulica


[Files]
Source: "build\AsignaciónÁulica\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\Asignación Áulica"; Filename: "{app}\main.exe"
Name: "{group}\Desinstalar Asignación Áulica"; Filename: "{uninstallexe}"
Name: "{autodesktop}\Asignación Áulica"; Filename: "{app}\main.exe"

; Configuración para generar el instalador con Inno Setup.
; Esta configuración se usa en el CI de GitHub.

[Setup]
AppName=Asignación Áulica
AppVersion=esto se completa en el CI

SetupIconFile=assets/iconos/unrn.ico
WizardStyle=modern

OutputDir=.\
OutputBaseFilename=Instalador-AsignaciónÁulica

; Instalar en "Program Files" del usuario:
DefaultDirName={autopf}\AsignaciónÁulica

[Languages]
Name: "es"; MessagesFile: "compiler:Languages\Spanish.isl"

[Files]
Source: "build\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\Asignación Áulica"; Filename: "{app}\main.exe"
Name: "{group}\Desinstalar Asignación Áulica"; Filename: "{uninstallexe}"
Name: "{userdesktop}\Asignación Áulica"; Filename: "{app}\main.exe"
